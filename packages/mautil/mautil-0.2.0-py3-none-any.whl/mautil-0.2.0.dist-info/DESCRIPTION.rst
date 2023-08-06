# mautil
An deep learning util based on tensroflow.
- easy to build model and do experiments
- easy to debug
- no need to transfer data to tf records

# requirements
tensorflow >= 1.11

# Install
`pip install mautil`

# Demo
- There are two text style transfer models. CA is an implementation of the  paper  [Style Transfer from Non-Parallel Text byCross-Alignment](https://papers.nips.cc/paper/7259-style-transfer-from-non-parallel-text-by-cross-alignment.pdf). CAR model just use reinforcement learning to bypass gumbel softmax
- run the text style transfer model in debug mode

  `python train.py -m CAR -dataset yelp -d`


