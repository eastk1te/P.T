import torch
import matplotlib.pyplot as plt
import argparse
from tqdm import tqdm 
import imageio
from IPython.display import Image
from IPython import display
import os 

def parse_opt():
    parser = argparse.ArgumentParser()
    
    # miscellaneous arguments for training
    parser.add_argument("--is_train", type=bool, default=True)
    parser.add_argument("--num_threads", type=int, default=24)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--random_seed", type=int, default=0)

    # training details
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--n_epochs", type=int, default=100)
    parser.add_argument("--lr", type=float, default=.0001)
    parser.add_argument("--momentum", type=float, default=.8)
    parser.add_argument("--is_trained", type=bool, default=False)

    # save file    
    parser.add_argument("--checkpoint_dir", type=str, default="./weights")
    parser.add_argument("--checkpoint", type=str, default="./weights/checkpoint.pt")
    parser.add_argument("--log_loss_dir", type=str, default="./log_loss/")

    # Image parameters
    parser.add_argument("--img_size", type=int, default=32)
    parser.add_argument("--n_classes", type=int, default=10)

    opt = parser.parse_args(args=[])

    return opt

def train(model, dataloader, criterion, optimizer, device):

    model.train()

    train_loss = 0.0

    for inputs, labels in tqdm(dataloader, desc='Training'):
        
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        # 순전파 및 손실 계산
        outputs, _ = model(inputs)
        loss = criterion(outputs, labels)

        # 역전파 및 가중치 갱신
        loss.backward()
        optimizer.step()

        train_loss += loss.item()

    train_loss /= len(dataloader)

    return model, optimizer, train_loss

def evaluate(model, test_dataloader, criterion, device):
    model.eval()  # 평가 모드로 설정

    eval_loss = 0.0

    with torch.no_grad():
        for inputs, labels in tqdm(test_dataloader, desc='Testing'):
            inputs, labels = inputs.to(device), labels.to(device)

            # 순전파 및 손실 계산
            outputs, _ = model(inputs)
            loss = criterion(outputs, labels)

            eval_loss += loss.item()

    eval_loss /= len(test_dataloader)

    return model, eval_loss

def train_loop(opt, model, train_dataloader, test_loader, optimizer, criterion, device):

    os.makedirs(opt.checkpoint_dir, exist_ok=True)
    os.makedirs(opt.log_loss_dir, exist_ok=True)

    # Initialize an empty list to store the loss values
    train_loss_history= []
    eval_loss_history= []

    gif_img = []

    # Training loop
    for epoch in tqdm(range(opt.n_epochs), desc='Epochs'):

        # training
        model, optimizer, train_loss = train(model, train_dataloader, criterion, optimizer, device)

        # validation
        with torch.no_grad():
            model, eval_loss = evaluate(model, test_loader, criterion, device)
        
        train_loss_history.append(train_loss)
        eval_loss_history.append(eval_loss)

        # logging
        description = f'Epoch: [{epoch + 1}/{opt.n_epochs}], \
                        Train Loss: {train_loss:.6f}, \
                        Test Loss: {eval_loss:.6f}' \

        tqdm.write(description)

        # Update the loss graph
        fig = plt.figure(figsize=(6,4), dpi=80)

        update_plot(train_loss_history, eval_loss_history, opt.n_epochs)

        # Read the temporary file as an image
        image = imageio.imread('temp.png')

        # Append the image to the GIF
        gif_img.append(image)
        # Display the updated graph
        display.clear_output(wait=True)
        display.display(plt.gcf())
        
    # Clear the final graph after the loop
    display.clear_output(wait=True)
    plt.close(fig)

    # Save the GIF file
    log_loss = os.path.join(opt.log_loss_dir, 'log_loss.gif')
    imageio.mimsave(log_loss , gif_img,'GIF', duration=500)
    display.display(Image(filename=log_loss))

    # checkpoint 저장
    checkpoint_path = os.path.join(opt.checkpoint_dir, 'checkpoint.pt')
    save_model(model, checkpoint_path)


def update_plot(x, y, xlim):
    # Clear the current plot
    plt.clf()

    # Update the plot
    plt.plot(x, color='blue', label=f'Train Loss : {x[-1]:.6f}')
    plt.plot(y, color='red', label=f'Eval Loss : {y[-1]:.6f}')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.xlim(0, xlim - 1)
    plt.ylim(0, 1)
    plt.title('Real-time Loss Graph')
    plt.legend()
    
    # Save the figure to a temporary file
    plt.savefig('temp.png')

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(model, path):
    model.load_state_dict(torch.load(path))