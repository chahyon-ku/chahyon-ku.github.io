---
layout: page
title: Primate Pose Estimation with Open Monkey Challenge
description: Reimplement and compare HRNet and ViTPose <br> Basic domain randomization (RandAugment) <br> Learned species special tokens
img: assets/projects/omc/preview.png
importance: 1
category: vision
---

<h5 class="row justify-content-sm-center">
Chahyon Ku, Gustav Baumgart, Maximilian Scheder-Bieschin
</h5>
<h5 class="row justify-content-sm-center">
University of Minnesota, Twin Cities
</h5>

[Proposal Paper](/assets/projects/omc/proposal_paper.pdf) <br>
[Proposal Slides](/assets/projects/omc/proposal_slides.pdf) <br>
[Final Paper](/assets/projects/omc/final_paper.pdf) <br>
[Final Slides](/assets/projects/omc/final_slides.pdf) <br>
[Code](https://github.com/chahyon-ku/openmonkeychallenge) <br>

## Introduction

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_motivation.png" title="slide_motivation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

[OpenMonkeyChallenge](http://openmonkeychallenge.com/) is a benchmark challenge for 2D non-human primate pose estimation (Yao et al).
It consists of 111,529 photographs labeled with 17 body landmarks and is the largest non-human primate image dataset, both in number of images and number of species included.
Non-human primate pose estimation is seen as more challenging than human pose estimation because non-human primates have more variation in their joint ranges and body geometry.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_dataset.png" title="slide_dataset" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Metrics

We used probability of correct keypoint (PCK@ϵ with ϵ = 0.2) and average mean per joint position error  (MPJPE) as performance metrics.
PCK@ϵ is a way of measuring how likely it is for the model to predict any joint’s position.
MPJPE calculates the mean distance of the predicted joint position from the actual joint position.
Both of these metrics normalize by the size of the bounding box W, but in different ways.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_metric.png" title="slide_metric" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Baseline
For the baseline we reimplemented [HRNet](https://jingdongwang2017.github.io/Projects/HRNet/PoseEstimation.html), as it is one of the best baseline models from the original OpenMonkeyChallenge paper, with average precision of 0.78 (Sun et al).
Unlike previous methods that traversed lowto-high or high-to-low resolutions, HRNet proposed a new architecture that maintained high-resolution representations through the entire model.
This led to two benefits as compared to existing models (1) improved spatial precision due to not needing to recover resolution (2) improved capabilities for pose estimation due to repeated multiscale fusions.

For our baseline, we fine-tuned 4 versions of HRNet as
provided by the timm library: w18, w32, w48, and w64.
We trained them for 20 epochs and evaluated the model that
had the lowest validation loss.
**This brings us to 3rd place in the leaderboard at 0.061
MPJPE for HRNet w64.**

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_hrnet.png" title="slide_hrnet" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## ViTPose and Improvements

We reimplemented ViTPose (Xu et al) as our main method.
This model was selected as it has not yet been applied to the task of non-human primate pose estimation and has recently produced state-of-the-art performance for human pose estimation.
They achieved a significant performance improvement against other state-of-the-art methods on the COCO validation set, and we hoped to improve on this model to beat the top-performing model on the OpenMonkeyChallenge leaderboard.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_vitpose.png" title="slide_vitpose" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

We fine-tune ImageNet-pretrained ViT-base for our ViTPose unless otherwise indicated. As our first set of experiments with ViTPose, we experiment with two hyperparameters: heatmap size and number of UpConv (transpose convolution) layers.
To speed up the process of finding the right parameter, we do not train until convergence but rather train for 5 epochs.
**This brings us to 2nd place in the leaderboard at 0.051 MPJPE for ViTPose with 4 UpConv layers.**

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_randaugment.png" title="slide_randaugment" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_token.png" title="slide_token" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

To further improve performance, we propose two additions to ViTPose: RandAugment and Specie Context Tokens. All models in this section are trained for 10 epochs.
First, we observed that the validation performance
plateaus and starts decreasing around the 5th epoch. Adding
RandAugment slows down the training, but allows the
model to learn past the non-augmented limit where the
model starts to overfit. We vary the magnitude m of the augmentation, which defines how skewed or jittered the color
and shape of the image is, to 0 (no augmentation), 2, 4 and
find that magnitude of 2 is the most effective in improving
the performance.
Second, we propose specie context tokens to utilize the
provided specie information. Adding context c, even though
it requires a minuscule (26K) number of extra parameters
and no additional computation, improved the performance
for all magnitudes of data augmentation.

## Conclusion

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/omc/slide_final.png" title="slide_final" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Using the methods and parameters we verified in the previous two sections, we train larger models for 20 epochs to
report our final performance. To specify, heatmap size s of
8, rand augment magnitude m of 2, and specie context prefix token are all used for ViT-base and ViT-large with 3 and
4 UpConv layers.
**This brings us to 1st place in the leaderboard at 0.045
MPJPE for ViTPose-large with 4 UpConv layers.**

### References
Yuan Yao, Abhiraj Mohan, Eliza Bliss-Moreau, Kristine Coleman, Sienna M. Freeman, Christopher J. Machado, Jessica Raper, Jan Zimmermann, Benjamin Y. Hayden, and Hyun Soo Park. Openmonkeychallenge: Dataset and benchmark challenges for pose tracking of non-human primates. bioRxiv, 2021.

Ke Sun, Bin Xiao, Dong Liu, and Jingdong Wang. Deep high-resolution representation learning for human pose estimation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 5693–5703, 2019.

Yufei Xu, Jing Zhang, Qiming Zhang, and Dacheng Tao. Vitpose: Simple vision transformer baselines for human pose
estimation, 2022.