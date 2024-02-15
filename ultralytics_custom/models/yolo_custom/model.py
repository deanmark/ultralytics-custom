from ultralytics.models import YOLO

from ultralytics_custom.models import yolo_custom


class YOLO_custom(YOLO):
    @property
    def task_map(self):
        tm = super().task_map
        tm["detect"]["trainer"] = yolo_custom.detect.CustomDetectionTrainer
        return tm
