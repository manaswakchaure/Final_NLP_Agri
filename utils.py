import torch
import torchvision.transforms as transforms
from PIL import Image


def print_examples(model, device, dataset):
    transform = transforms.Compose(
        [
            transforms.Resize((299, 299)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    model.eval()
    test_img1 = transform(Image.open("test_examples/dog.jpg").convert("RGB")).unsqueeze(
        0
    )
    print("Example 1 CORRECT: Dog on a beach by the ocean")
    print(
        "Example 1 OUTPUT: "
        + " ".join(model.caption_image(test_img1.to(device), dataset.vocab))
    )
    test_img2 = transform(
        Image.open("test_examples/1.jpg").convert("RGB")
    ).unsqueeze(0)
    print("Example 2 CORRECT: A women is planting a crop in the farm")
    print(
        "Example 2 OUTPUT: "
        + " ".join(model.caption_image(test_img2.to(device), dataset.vocab))
    )
    test_img3 = transform(Image.open("test_examples/2.jpg").convert("RGB")).unsqueeze(
        0
    )
    print("Example 3 CORRECT: A man is watering the crop in the farm")
    print(
        "Example 3 OUTPUT: "
        + " ".join(model.caption_image(test_img3.to(device), dataset.vocab))
    )
    test_img4 = transform(
        Image.open("test_examples/3.jpg").convert("RGB")
    ).unsqueeze(0)
    print("Example 4 CORRECT: A man is monitoring the crop in the farm")
    print(
        "Example 4 OUTPUT: "
        + " ".join(model.caption_image(test_img4.to(device), dataset.vocab))
    )
    test_img5 = transform(
        Image.open("test_examples/4.jpg").convert("RGB")
    ).unsqueeze(0)
    print("Example 5 CORRECT: A man is spraying fertilizer in the farm")
    print(
        "Example 5 OUTPUT: "
        + " ".join(model.caption_image(test_img5.to(device), dataset.vocab))
    )
    test_img6 = transform(
        Image.open("test_examples/5.jpg").convert("RGB")
    ).unsqueeze(0)
    print("Example 6 CORRECT: A girl is picking fruit from the tree")
    print(
        "Example 6 OUTPUT: "
        + " ".join(model.caption_image(test_img6.to(device), dataset.vocab))
    )
    model.train()


def save_checkpoint(state, filename="my_checkpoint.pth.tar"):
    print("=> Saving checkpoint")
    torch.save(state, filename)


def load_checkpoint(checkpoint, model, optimizer):
    print("=> Loading checkpoint")
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    step = checkpoint["step"]
    return step
