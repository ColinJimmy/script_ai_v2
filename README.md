# Handwritten Text Recognition with TensorFlow

This project implements a Handwritten Text Recognition (HTR) system using TensorFlow. The implemented model takes images of handwritten texts and transcribes them into digital text.

## Project Overview

- **Implementation**: Deep Neural Network with CNN, RNN and CTC layers
- **Framework**: TensorFlow
- **Model Architecture**: CNN + RNN + CTC
- **Additional Tools**: 
  - Word Beam Search Decoding
  - Custom data loader for efficient image processing

## Getting Started

### Prerequisites
1. Install required packages by running:
```
pip install -r requirements.txt
```

### Running the Project

1. **Download Pre-trained Model**
   - Download from model repository
   - Place in the `model` directory

2. **Inference**
   ```python
   # Load and use the model
   python main.py
   ```

3. **Training**
   - Prepare IAM dataset according to documentation
   - Adjust model parameters if needed
   - Start training process

## Model Details

The model combines the following components:
- CNN: Feature extraction from input images
- RNN: Sequence processing for text recognition 
- CTC: Alignment of text with the input sequence

Word beam search decoding is integrated to improve accuracy by incorporating dictionary and language model.