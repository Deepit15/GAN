from argparse import ArgumentParser

import torch
import yaml
from pytorch_lightning import Trainer

from gan_module import AgingGAN

parser = ArgumentParser()
parser.add_argument('--config', default='configs/aging_gan.yaml', help='Config to use for training')


def main():
    args = parser.parse_args()
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    print(config)
    model = AgingGAN(config)
    trainer = Trainer(max_epochs=config['epochs'], accelerator="gpu",devices=1, auto_scale_batch_size='binsearch')
    trainer.fit(model)
    torch.save(model.state_dict(), 'pretrained_model/state_dict.pth')
    # torch.save(gen.state_dict(),'pretrained_model/state_dict.pth')
    # torch.save(gen.state_dict(),'pretrained_model/state_dict.pth')


if __name__ == '__main__':
    main()
