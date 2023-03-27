---
layout: page
title: Multilingual Complex Named Entity Recognition with Data and Context Augmentation
description: Extend pretrained language model (XLM-RoBERTa) <br> Data augmentation with Google Translate API (MulDA) <br> Context augmentation with Elasticsearch on Wikipedia (KB-NER)
img: assets/projects/multiconer/preview.png
importance: 1
category: nlp
---

<h5 class="row justify-content-sm-center">
Chahyon Ku, London Lowmanstone IV, Asal Shavandi, Josh Spitzer-Resnick 
</h5>
<h5 class="row justify-content-sm-center">
University of Minnesota, Twin Cities
</h5>

[Proposal Paper](/assets/projects/multiconer/proposal_paper.pdf) <br>
[Proposal Slides](/assets/projects/multiconer/proposal_slides.pdf) <br>
[Midterm Paper](/assets/projects/multiconer/midterm_paper.pdf) <br>
[Final Paper](/assets/projects/multiconer/final_paper.pdf) <br>
[Final Slides](/assets/projects/multiconer/final_slides.pdf) <br>
[Code](https://github.com/chahyon-ku/polygots) <br>

### Extended XLM-RoBERTA + Conditional Random Field (CRF) baseline with data and context augmentation
#### Data Augmentation
Translation based data augmentation with Google Cloud API (MulDA), utilizing multilingual dataset.
#### Context Augmentation
Following procedures of KB-NER[1], we use Elasticsearch to index Wikipedia articles in 100 languages and use the index to augment the training data with context information.


<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/multiconer/final_slides/final_slides-03.png" title="poster" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/multiconer/final_slides/final_slides-10.png" title="poster" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/multiconer/final_slides/final_slides-15.png" title="poster" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/multiconer/final_slides/final_slides-20.png" title="poster" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/projects/multiconer/final_slides/final_slides-21.png" title="poster" class="img-fluid rounded z-depth-1" %}
    </div>
</div>