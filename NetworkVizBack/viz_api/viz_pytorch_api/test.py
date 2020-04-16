import torch
import viz_api.viz_pytorch_api.input as input
import viz_api.viz_pytorch_api.layer as layer
import viz_api.viz_pytorch_api.tensor as tensor
import viz_api.viz_pytorch_api.optimizer as optimizer

epochs = 1
input_size = 784
output_size = 10
hidden_sizes = [128, 64]

device = torch.device("cuda:0")
# model layer structure

linear1 = layer.Linear_Torch(in_features=input_size, out_features=hidden_sizes[0], device=device)
relu1 = layer.ReLU_Torch(device=device)
linear2 = layer.Linear_Torch(in_features=hidden_sizes[0], out_features=hidden_sizes[1], device=device)
relu2 = layer.ReLU_Torch(device=device)
linear3 = layer.Linear_Torch(in_features=hidden_sizes[1], out_features=output_size, device=device)
logsoftmax1 = layer.LogSoftmax_Torch(dim=1, device=device)


# model input
root="../../static/dataset/"
batch_size=64
shuffle=True
train=True
download=True
device=device
model_input = input.MnistDataSetLoader_Torch(root="../../static/dataset/", batch_size=64, shuffle=True, train=True, download=True, device=device)

# model loss

# model optimizer

# model iteration
for epoch in range(epochs):
    for iteration in range(model_input.get_number_batch()):
        image = model_input.get_loaded_tensor_img_single(iteration)
        image.set_linked_tensor(image.get_linked_tensor().view(batch_size, -1))

        linear1_output = linear1.forward(image, inplace=False)
        relu1_output = relu1.forward(linear1_output, inplace=False)
        linear2_output = linear2.forward(relu1_output, inplace=True)
        relu2_output = relu2.forward(linear2_output, inplace=False)
        linear3_output = linear3.forward(relu2_output, inplace=True)
        logsoftmax1_output = logsoftmax1.forward(linear3_output, inplace=True)

        print(logsoftmax1_output.get_linked_tensor())
        break
    break