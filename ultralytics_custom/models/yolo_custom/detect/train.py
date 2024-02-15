from ultralytics.models.yolo.detect.train import DetectionTrainer
from ultralytics.utils import (LOGGER)


class CustomDetectionTrainer(DetectionTrainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_callback("on_fit_epoch_end", on_fit_epoch_end)


def on_fit_epoch_end(trainer):
    if trainer.best_fitness == trainer.fitness:
        LOGGER.info("(*) best")
