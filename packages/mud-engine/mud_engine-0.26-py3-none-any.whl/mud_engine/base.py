import logging

_HEARTBEATS = {}

class MUDFactory(object):
    pass

class MUDObject(object):

    heartbeat = None

    def __init__(self):
        if self.heartbeat:
            _HEARTBEATS[self] = self.heartbeat

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join([str(k) + "=" + str(v) for k,v in self.__dict__.items()]))

    def __del__(self):

        self._deregister_heartbeat()
        logging.debug("Deleting {}".format(self))

    def _deregister_heartbeat(self):
        if self in _HEARTBEATS:
            del _HEARTBEATS[self]

class MUDAction(MUDObject):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        acts = self.function(*args, **kwargs)
        if not isinstance(acts, list) or not isinstance(acts, tuple):
            return [acts]
        return acts

class MUDActionException(Exception):
    pass

class StopAction(MUDActionException):
    pass

class MUDEvent(MUDObject):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)

class MetaMUDInterface(type):
    _INTERFACES = {}

    def __new__(cls, name, bases, dct):
        inst = super().__new__(cls, name, bases, dct)
        if inst.name:
            cls._INTERFACES[inst.name] = inst
        return inst

class MUDInterface(object, metaclass=MetaMUDInterface):

    name = None
    engine = None

    @classmethod
    def get_interface(cls, name):
        interface = MetaMUDInterface._INTERFACES.get(name)
        if not interface:
            raise Exception("Attempting to access interface {}, which doesn't exist".format(name))
        return interface

    def __del__(self):
        logging.debug("Deleting {}".format(self))

    def __getattribute__(self, k):

        import inspect

        v = object.__getattribute__(self, k)
        if k == "engine" and not v:
            v = self.__class__.engine
            if not v:
                raise Exception("Engine not instantiated yet")
            setattr(self, k, v)
        elif not k.startswith("__") and inspect.isclass(v):
            v = v()
            setattr(self, k, v)
        return v

    def __init__(self):
        self.engine = None
        for k,v in MetaMUDInterface._INTERFACES.items():
            setattr(self, k, v)
