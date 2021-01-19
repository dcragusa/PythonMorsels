
# def instance_tracker():
#     class TrackInstances:
#         instances = []
#         def __init__(self, *args, **kwargs):
#             TrackInstances.instances.append(self)
#             super().__init__(*args, **kwargs)
#     return TrackInstances


# def instance_tracker(instances_name='instances'):
#     class TrackInstances:
#         def __init__(self, *args, **kwargs):
#             getattr(TrackInstances, instances_name).append(self)
#             super().__init__(*args, **kwargs)
#     setattr(TrackInstances, instances_name, [])
#     return TrackInstances


# def instance_tracker(instances_name='instances'):
#     class TrackInstances:
#         def __new__(cls, *args, **kwargs):
#             instance = super().__new__(cls)
#             getattr(TrackInstances, instances_name).append(instance)
#             return instance
#     setattr(TrackInstances, instances_name, [])
#     return TrackInstances


from weakref import WeakSet


def instance_tracker(instances_name='instances'):
    class TrackInstances:
        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            getattr(TrackInstances, instances_name).add(instance)
            return instance
    setattr(TrackInstances, instances_name, WeakSet())
    return TrackInstances
