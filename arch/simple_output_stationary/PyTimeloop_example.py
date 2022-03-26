from pytimeloop.config import ConfigDict
from pytimeloop.app import MapperApp

config = ConfigDict.load_yaml_files(['arch/*.yaml', 'arch/components/*.yaml',
                                     'constraints/*.yaml',
                                     '../../layer_shapes/AlexNet/AlexNet_layer1.yaml',
                                     'mapper/mapper.yaml'])

mapper = MapperApp(config, '.')

mapper.run()
