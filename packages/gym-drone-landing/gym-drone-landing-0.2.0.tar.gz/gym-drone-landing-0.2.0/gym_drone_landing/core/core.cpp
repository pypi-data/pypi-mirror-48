#include <Python.h>
#include <Box2D/Box2D.h>

struct Scene {
    PyObject_HEAD
    b2World * world;
    b2Body * drone;
    b2ContactListener * contact_listener;

    int frames_left;
    float score;
};

PyTypeObject * Scene_type;

class DroneContactListener : public b2ContactListener {
    Scene * scene;
    b2Body * start;
    b2Body * target;

public:
    DroneContactListener(Scene * scene, b2Body * start, b2Body * target): scene(scene), start(start), target(target) {
    }

    void BeginContact(b2Contact * contact) {
        b2Fixture * self = scene->drone->GetFixtureList();
        b2Fixture * other = contact->GetFixtureB() == self ? contact->GetFixtureA() : contact->GetFixtureB();
        if (other == start->GetFixtureList()) {
            return;
        }
        if (other == target->GetFixtureList()) {
            float linear_velocity = scene->drone->GetLinearVelocity().Length();
            float angular_velocity = scene->drone->GetAngularVelocity();
            float delta_pos = fabsf(target->GetPosition().x - scene->drone->GetPosition().x);
            float delta_angle = fabsf(target->GetAngle());
            if (delta_pos < 0.3) {
                float x = linear_velocity * 0.3f + fabsf(angular_velocity) * 0.3f + delta_pos * 0.1f + delta_angle * 0.5f;
                scene->score = 0.1f + logf(1.0f + expf(-x));
            }
        }
        scene->frames_left = 0;
    }
};

inline b2Body * static_box(b2World * world, float x, float y, float w, float h) {
    b2BodyDef body_def;
    body_def.position.Set(x, y);
    b2Body * body = world->CreateBody(&body_def);
    b2PolygonShape box;
    box.SetAsBox(w, h);
    body->CreateFixture(&box, 0.0f);
    return body;
}

Scene * core_meth_scene(PyObject * self, PyObject * args, PyObject * kwargs) {
    static char * keywords[] = {"shift", NULL};

    float shift;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "f", keywords, &shift)) {
        return NULL;
    }

    Scene * scene = PyObject_New(Scene, Scene_type);

    scene->score = 0.0f;
    scene->frames_left = 400;
    scene->world = new b2World({0.0f, -10.0f});

    static_box(scene->world, 0.0f, -10.0f, 10.0f, 10.0f);
    b2Body * start = static_box(scene->world, -3.0f, 0.2f, 0.6f, 0.2f);
    b2Body * target = static_box(scene->world, 3.0f, 0.2f, 0.6f, 0.2f);

    b2BodyDef drone_def;
    drone_def.type = b2_dynamicBody;
    drone_def.position.Set(-3.0f + shift, 0.52f);
    scene->drone = scene->world->CreateBody(&drone_def);

    b2PolygonShape drone_box;
    drone_box.SetAsBox(0.4f, 0.1f);

    b2FixtureDef fixture_def;
    fixture_def.shape = &drone_box;
    fixture_def.density = 1.0f;
    fixture_def.friction = 0.3f;

    scene->drone->CreateFixture(&fixture_def);

    scene->contact_listener = new DroneContactListener(scene, start, target);
    scene->world->SetContactListener(scene->contact_listener);

    return scene;
}

PyObject * Scene_meth_step(Scene * self, PyObject * action) {
    PyObject * left_action = PySequence_GetItem(action, 0);
    PyObject * right_action = PySequence_GetItem(action, 1);
    double left_magnitude = PyFloat_AsDouble(left_action) * 0.4 + 0.7;
    double right_magnitude = PyFloat_AsDouble(right_action) * 0.4 + 0.7;
    Py_DECREF(left_action);
    Py_DECREF(right_action);
    b2Vec2 left_force = self->drone->GetWorldVector({0.0f, (float)left_magnitude});
    b2Vec2 right_force = self->drone->GetWorldVector({0.0f, (float)right_magnitude});
    b2Vec2 left_point = self->drone->GetWorldPoint({-0.3f, 0.0f});
    b2Vec2 right_point = self->drone->GetWorldPoint({0.3f, 0.0f});
    self->drone->ApplyForce(left_force, left_point, true);
    self->drone->ApplyForce(right_force, right_point, true);
    self->world->Step(1.0f / 60.0f, 6, 2);
    self->frames_left -= 1;
    float x = self->drone->GetPosition().x;
    float y = self->drone->GetPosition().y;
    float angle = self->drone->GetAngle();
    bool done = self->frames_left <= 0 || x < -5.5f || x > 5.5f || y > 5.5f;
    PyObject * observation = Py_BuildValue("(ff)f", x, y, angle);
    return Py_BuildValue("NfO{}", observation, self->score, done ? Py_True : Py_False);
}

inline PyObject * build_box(b2PolygonShape * shape) {
    b2Vec2 a = shape->GetVertex(0);
    b2Vec2 b = shape->GetVertex(1);
    b2Vec2 c = shape->GetVertex(2);
    b2Vec2 d = shape->GetVertex(3);
    return Py_BuildValue("(ff)(ff)(ff)(ff)", a.x, a.y, b.x, b.y, c.x, c.y, d.x, d.y);
}

PyObject * Scene_meth_polygons(Scene * self) {
    int num_bodies = self->world->GetBodyCount();
    b2Body * body = self->world->GetBodyList();
    PyObject * res = PyList_New(num_bodies);
    for (int i = 0; i < num_bodies; ++i) {
        b2Fixture * fixture = body->GetFixtureList();
        b2PolygonShape * shape = (b2PolygonShape *)fixture->GetShape();
        PyList_SET_ITEM(res, i, build_box(shape));
        body = body->GetNext();
    }
    return res;
}

PyObject * Scene_meth_transforms(Scene * self) {
    int num_bodies = self->world->GetBodyCount();
    b2Body * body = self->world->GetBodyList();
    PyObject * res = PyList_New(num_bodies);
    for (int i = 0; i < num_bodies; ++i) {
        b2Vec2 position = body->GetPosition();
        float32 angle = body->GetAngle();
        PyList_SET_ITEM(res, i, Py_BuildValue("fff", position.x, position.y, angle));
        body = body->GetNext();
    }
    return res;
}

void Scene_dealloc(Scene * self) {
    delete self->world;
    delete self->contact_listener;
    Py_TYPE(self)->tp_free(self);
}

PyMethodDef Scene_methods[] = {
    {"step", (PyCFunction)Scene_meth_step, METH_O, NULL},
    {"polygons", (PyCFunction)Scene_meth_polygons, METH_NOARGS, NULL},
    {"transforms", (PyCFunction)Scene_meth_transforms, METH_NOARGS, NULL},
    {0},
};

PyType_Slot Scene_slots[] = {
    {Py_tp_methods, (void *)Scene_methods},
    {Py_tp_dealloc, (void *)Scene_dealloc},
    {0},
};

PyType_Spec Scene_spec = {"gym_drone_landing.core.Scene", sizeof(Scene), 0, Py_TPFLAGS_DEFAULT, Scene_slots};

PyMethodDef module_methods[] = {
    {"scene", (PyCFunction)core_meth_scene, METH_VARARGS | METH_KEYWORDS, NULL},
    {NULL},
};

PyModuleDef module_def = {PyModuleDef_HEAD_INIT, "gym_drone_landing.core", NULL, -1, module_methods};

extern "C" PyObject * PyInit_core() {
    PyObject * module = PyModule_Create(&module_def);
    Scene_type = (PyTypeObject *)PyType_FromSpec(&Scene_spec);
    PyModule_AddObject(module, "Scene", (PyObject *)Scene_type);
    return module;
}
