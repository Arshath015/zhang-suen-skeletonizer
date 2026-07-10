from typing import Tuple
from zhang_suen_skeletonizer import Skeletonizer
from data_io import DataIO

class Orchestrator:
    def __init__(self):
        self.skeletonizer = Skeletonizer()
        self.data_io = DataIO()
    def run(self, input_filename: str, output_filename: str) -> None:
        input_image = self.data_io.read_image(input_filename)
        output_skeleton = self.skeletonizer.skeletonize(input_image)
        self.data_io.write_image(output_filename, output_skeleton)