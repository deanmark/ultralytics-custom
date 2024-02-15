import sys

from ultralytics.cfg import entrypoint as ep

from ultralytics_custom import YOLO_custom


def entrypoint(debug="", arch=YOLO_custom):
    ep(debug=debug, arch=arch)


if __name__ == "__main__":
    # Example: entrypoint(debug='yolo predict model=yolov8n.pt')
    entrypoint(debug="")
