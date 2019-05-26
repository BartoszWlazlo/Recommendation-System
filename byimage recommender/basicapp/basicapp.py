import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image

pic_one = str(input("Podaj nazwe pliku 1\n"))
pic_two = str(input("Podaj nazwe pliku 2\n"))

model = models.resnet18(pretrained=True)

layer = model._modules.get('avgpool')

model.eval()

scaler = transforms.Resize((224, 224))
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
to_tensor = transforms.ToTensor()

def get_vector(image_name):

    img = Image.open(image_name)

    t_img = Variable(normalize(to_tensor(scaler(img))).unsqueeze(0))

    my_embedding = torch.zeros(512)

    def copy_data(m, i, o):
        my_embedding.copy_(o.data.squeeze())

    h = layer.register_forward_hook(copy_data)

    model(t_img)

    h.remove()

    return my_embedding

pic_one_vector = get_vector(pic_one)
pic_two_vector = get_vector(pic_two)


cos = nn.CosineSimilarity(dim=1, eps=1e-6)
cos_sim = cos(pic_one_vector.unsqueeze(0),
              pic_two_vector.unsqueeze(0))
print('\nCosine similarity: {0}\n'.format(cos_sim))

