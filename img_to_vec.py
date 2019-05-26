import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms


class Img2Vec():

    def __init__(self, cuda=False, model='resnet-18', layer='default', layer_output_size=512):
        self.device = torch.device("cuda" if cuda else "cpu")
        self.layer_output_size = layer_output_size
        self.model_name = model
        
        self.model, self.extraction_layer = self._get_model_and_layer(model, layer)

        self.model = self.model.to(self.device)

        self.model.eval()

        self.scaler = transforms.Resize((224, 224))
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                              std=[0.229, 0.224, 0.225])
        self.to_tensor = transforms.ToTensor()

    def get_vec(self, img, tensor=False):
        image = self.normalize(self.to_tensor(self.scaler(img))).unsqueeze(0).to(self.device)

        if self.model_name == 'alexnet':
            my_embedding = torch.zeros(1, self.layer_output_size)
        else:
            my_embedding = torch.zeros(1, self.layer_output_size, 1, 1)

        def copy_data(m, i, o):
            my_embedding.copy_(o.data)

        h = self.extraction_layer.register_forward_hook(copy_data)
        h_x = self.model(image)
        h.remove()

        if tensor:
            return my_embedding
        else:
            if self.model_name == 'alexnet':
                return my_embedding.numpy()[0, :]
            else:
                return my_embedding.numpy()[0, :, 0, 0]

    def _get_model_and_layer(self, model_name, layer):

        if model_name == 'resnet-18':
            model = models.resnet18(pretrained=True)
            if layer == 'default':
                layer = model._modules.get('avgpool')
                self.layer_output_size = 512
            else:
                layer = model._modules.get(layer)

            return model, layer

        elif model_name == 'alexnet':
            model = models.alexnet(pretrained=True)
            if layer == 'default':
                layer = model.classifier[-2]
                self.layer_output_size = 4096
            else:
                layer = model.classifier[-layer]

            return model, layer

        else:
            raise KeyError('Model %s was not found' % model_name)
