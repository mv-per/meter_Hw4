# meter_Hw4

This repository contains the code and resources for Assignment #4, focusing on developing an Artificial Neural Network (ANN) package with inheritance.

## Getting Started

### Initial Setup

1. Fork the Repository

```bash
# First, fork the repository on GitHub by clicking the 'Fork' button at:
https://github.com/gabi107/meter_Hw4

# Then clone your forked version
git clone https://github.com/YOUR-USERNAME/meter_Hw4.git
cd meter_Hw4
```

## Repository Structure and Usage

The repository is organized for developing an Artificial Neural Network (ANN) package with inheritance. Here's how to use it:

### 1. Explore the Data

- The dataset is available in the repository
- Use the provided Jupyter notebooks to familiarize yourself with the data structure

### 2. Development Process

- Create new branches for feature development

```bash
git checkout -b feature/your-feature-name
```

- Test your code in Jupyter notebooks first
- Once tested, integrate your code into the package structure

### 3. Running Tests

- Use the provided test notebooks to try different hyperparameter combinations
- Document your findings using markdown cells
- Test at least 4 combinations of:
  - hidden_layer_sizes
  - learning_rate_init
  - max_iter

### 4. Making Changes

```bash
# After making changes
git add .
git commit -m "Description of your changes"
git push origin feature/your-feature-name
```

## Tips for Success

### Version Control

- Make frequent, small commits
- Use clear commit messages
- Create separate branches for different features

### Documentation

- Comment your code
- Use markdown in notebooks to explain your findings
- Document any assumptions or decisions made

### Testing

- Test your code thoroughly in notebooks before integration
- Verify that inheritance is working correctly
- Ensure all visualization functions work as expected

## Troubleshooting

### Common Issues and Solutions

1. Package Import Errors

   - Check your Python path
   - Verify all dependencies are installed
   - Make sure you're in the correct virtual environment

2. Visualization Issues
   - Restart the Jupyter kernel
   - Check that matplotlib is properly configured
