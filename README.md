Here is my thesis on computer vision, which I presented in 2023 for a Bachelor's degree.

This project introduces a new scene text detection architecture focused on speed, which is a combination of different neural network models.

The texts of the paper and presentation are in Russian. Here's the abstract translated to English:

> The paper introduces a lightweight modification of the EAST neural network model, which allows to speed up the task of localization of text regions in images comprising sophisticated scenes. We present theoretical background associated with the most relevant methods of text localization and recognition. A CRNN+CTC-loss neural network model and an end-to-end model of text recognition on images based on EAST and CRNN+CTC-loss models are implemented and tested. We also proposed a lightweight modification of the end-to-end FOTS model based on the developed lightweight modification of the EAST model and the CRNN+CTC-loss model.

## MobileEAST implementation

Please reference to files:
- [model.py](https://github.com/avrtt/MobileEAST/blob/main/code/model.py)
- [utils.py](https://github.com/avrtt/MobileEAST/blob/main/code/utils.py) (main chunk of code)
- [train.py](https://github.com/avrtt/MobileEAST/blob/main/code/train.py)
- [inference.py](https://github.com/avrtt/MobileEAST/blob/main/code/inference.py)

## Publications

- [NSTU Library](https://elibrary.nstu.ru/source?id=181646)
- [Google Scholar](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=AGhTpfgAAAAJ&citation_for_view=AGhTpfgAAAAJ:u-x6o8ySG0sC)

## References

1. Deep Learning Based OCR for Text in the Wild // nanonets.com : сайт. – URL: https://nanonets.com/blog/deep-learning-ocr/ (дата обращения: 08.06.2023).
2. Rail OCR based on AI // www.supplai.nl : сайт. – URL: https://www.supplai.nl/en/products-ai/rail-ocr-automation/ (дата обращения: 08.06.2023).
3. Text Recognition in the Wild: A Survey / X. Chen, L. Jin, Y. Zhu [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/2005.03492. – Дата публикации: 03.12.2020.
4. Krizhevsky, A. ImageNet Classification with Deep Convolutional Neural Networks / A. Krizhevsky, I. Sutskever, G. E. Hinton // proceedings.neurips.cc : электронный журнал. – URL: https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf. – Дата публикации: 2012.
5. EAST: An Efficient and Accurate Scene Text Detector / X. Zhou, C. Yao, H. Wen [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1704.03155. – Дата публикации: 10.07.2017.
6. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications / A. G. Howard, M. Zhu, B. Chen [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1704.04861. – Дата публикации: 17.04.2017.
7. An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition / B. Shi, X. Bai, C. Yao [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1507.05717. – Дата публикации: 21.07.2015.
8. FOTS: Fast Oriented Text Spotting with a Unified Network / X. Liu, D. Liang, S. Yan [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1801.01671. – Дата публикации: 15.06.2018.
9. Задача нахождения объектов на изображении // neerc.ifmo.ru : сайт. – URL: https://neerc.ifmo.ru/wiki/index.php?title=Задача_нахождения_объектов_на_изображении (дата обращения: 08.06.2023).
10. Deep Residual Learning for Image Recognition / K. He, X. Zhang, S. Ren [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1512.03385. – Дата публикации: 10.12.2015.
11. Ioffe, S. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift / S. Ioffe, C. Szegedy // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1502.03167. – Дата публикации: 02.03.2015.
12. Kunishige, F. Scenery Character Detection with Environmental Context / F. Kunishige, F. Yaokai, S. Uchida // www.iapr-tc11.org : электронный журнал. – URL: http://www.iaprtc11.org/archive/icdar2011/fileup/PDF/4520b049.pdf. – Дата публикации: 2011.
13. Epshtein, B. Detecting Text in Natural Scenes with Stroke Width Transform / B. Epshtein, E. Ofek, Y. Wexler // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/224164328_Detecting_Text_in_Natural_Scenes_with_Stroke_Width_Transform. – Дата публикации: 2010.
14. Du, Y. Dot Text Detection Based on FAST Points / Y. Du, H. Ai, S. Lao // dblp.org : электронный журнал. – URL: https://dblp.org/rec/conf/icdar/DuAL11.html. – Дата публикации: 2011.
15. Text-attentional convolutional neural network for scene text detectio / T. He, W. Huang, Y. Qiao, J. Yao // arXiv.org : электронный журнал. – URL: https://arxiv.org/pdf/1510.03283.pdf. – Дата публикации: 2016.
16. Mask TextSpotter: An End-to-End Trainable Neural Network for Spotting Text with Arbitrary Shapes / M. Liao, P. Lyu, M. He [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1908.08207. – Дата публикации: 22.08.2019.
17. PhotoOCR : Reading Text in Uncontrolled Conditions / A. Bissacco, M. Cummins, Y. Netzer [и др.] // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/319770431_PhotoOCR_Reading_Text_in_Uncontrolled_Conditions. – Дата публикации: 2013.
18. Jaderberg, M. Deep Features for Text Spotting / M. Jaderberg, A. Vedaldi, A. Zisserman // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/319770170_Deep_Features_for_Text_Spotting. – Дата публикации: 2014.
19. Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition / M. Jaderberg, K. Simonyan, A. Vedaldi, A. Zisserman // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1406.2227. – Дата публикации: 09.12.2014.
20. Reading Text in the Wild with Convolutional Neural Networks / M. Jaderberg, K. Simonyan, A. Vedaldi, A. Zisserman // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1412.1842. – Дата публикации: 04.12.2014.
21. Multi-digit Number Recognition from Street View Imagery using Deep Convolutional Neural Networks / I. J. Goodfellow, B. Bulatov, J, Ibarz [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1312.6082. – Дата публикации: 14.04.2014.
22. Connectionist temporal classification: Labelling unsegmented sequence data with recurrent neural 'networks / A. Graves, S. Fernandez, F. Gomez, J. Schmidhuber // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/221346365_Connectionist_temporal_classification_Labelling_unsegmented_sequence_data_with_recurrent_neural_'networks. – Дата публикации: 2006.
23. Ghosh, S. Visual Attention Models for Scene Text Recognition / S. Ghosh, E. Valveny, A, Bagdanov // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/322780356_Visual_Attention_Models_for_Scene_Text_Recognition. – Дата публикации: 2017.
24. Scene Text Recognition with Sliding Convolutional Character Models / F. Yin, Y. Wu, X. Zhang, C. Liu // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1709.01727. – Дата публикации: 06.09.2017.
25. SCAN: Sliding Convolutional Attention Network for Scene Text Recognition / Y. Wu, F. Yin, X. Zhang [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1806.00578. – Дата публикации: 02.06.2018.
26. A Simple and Robust Convolutional-Attention Network for Irregular Text Recognition / P. Wang, L. Yang, H. Li [и др.] // www.semanticscholar.org : электронный журнал. – URL: https://www.semanticscholar.org/paper/ASimple-and-Robust-Convolutional-Attention-Network-WangYang/5bf577d7f378138d37a165cf764cb1967392cb65. – Дата публикации: 2019.
27. Liu, W. SAFE: Scale Aware Feature Encoder for Scene Text Recognition / W. Liu, C. Chen, K. Wong // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1901.05770. – Дата публикации: 17.06.2019.
28. The Challenge of Vanishing/Exploding Gradients in Deep Neural Networks // www.analyticsvidhya.com : сайт. – URL: https://www.analyticsvidhya.com/blog/2021/06/the-challenge-of-vanishingexploding-gradients-in-deep-neural-networks/ (дата обращения: 08.06.2023).
29. Deep Residual Learning for Image Recognition / K, He, X. Zhang, S. Ren, J. Sun // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1512.03385. – Дата публикации: 10.12.2015.
30. Overview - Incidental Scene Text // rrc.cvc.uab.es : сайт. – URL: https://rrc.cvc.uab.es/?ch=4&com=introduction (дата обращения: 08.06.2023).
31. Hosang, J. Learning non-maximum suppression / J. Hosang, R. Benenson, B. Schiele // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1705.02950. – Дата публикации: 09.05.2017.
32. PVANET: Deep but Lightweight Neural Networks for Real-time Object Detection / S. Hong, B. Roh, Y. Cheon [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1608.08021. – Дата публикации: 30.09.2017.
33. Xie, S. Holistically-Nested Edge Detection / S. Xie, Z. Tu // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1504.06375. – Дата публикации: 04.10.2015.
34. Scene Text Detection via Holistic, Multi-Channel Prediction / C. Yao, X. Bai, N. Sang [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1606.09002. – Дата публикации: 05.07.2016.
35. Intersection over Union (IoU) for object detection // pyimagesearch.com : сайт. – URL: https://pyimagesearch.com/2016/11/07/intersection-overunion-iou-for-object-detection/ (дата обращения: 08.06.2023).
36. Kingma, D. P. Adam: A Method for Stochastic Optimization / D. P. Kingma, J. Ba // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1412.6980. – Дата публикации: 30.01.2017.
37. Character Region Awareness for Text Detection / Y. Baek, B. Lee, D. Han [и др.] // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1904.01941. – Дата публикации: 03.04.2019.
38. Simonyan, K. Very Deep Convolutional Networks for Large-Scale Image Recognition / K. Simonyan, A. Zisserman // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1409.1556. – Дата публикации: 10.04.2015.
39. Shi, B. An End-to-End Trainable Neural Network for Image-Based Sequence Recognition and Its Application to Scene Text Recognition / B. Shi, X. Bai, C. Yao // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/280330424_An_End-toEnd_Trainable_Neural_Network_for_ImageBased_Sequence_Recognition_and_Its_Application_to_Scene_Text_Recognition. – Дата публикации: 2015.
40. Hochreiter, S. Long Short-term Memory / S. Hochreiter, J. Schmidhuber // ResearchGate : электронный журнал. – URL:
https://www.researchgate.net/publication/13853244_Long_Shortterm_Memory. – Дата публикации: 1997.
41. Kunishige, Y. Scenery Character Detection with Environmental Context / Y. Kunishige, F. Yaokai, S. Uchida // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/224265579_Scenery_Character_Detection_with_Environmental_Context. – Дата публикации: 2011.
42. Implementation of EAST scene text detector in Keras // GitHub : сайт. – URL: https://github.com/janzd/EAST (дата обращения: 08.06.2023).
43. Generalised Dice Overlap as a Deep Learning Loss Function for Highly Unbalanced Segmentations / C. H. Sudre, W. Li, T. Vercauteren [и др.] // ResearchGate : электронный журнал. – URL: https://www.researchgate.net/publication/319633097_Generalised_Dice_Overlap_as_a_Deep_Learning_Loss_Function_for_Highly_Unbalanced_Segmentations. – Дата публикации: 2017.
44. Convolutional recurrent neural network for scene text recognition or OCR in Keras // GitHub : сайт. – URL: https://github.com/janzd/CRNN (дата обращения: 08.06.2023).
45. Spatial Transformer Networks / M. Jaderberg, K. Simonyan, A. Zisserman, K. Kavukcuoglu // arXiv.org : электронный журнал. – URL: https://arxiv.org/abs/1506.02025. – Дата публикации: 04.02.2016.
46. How to Calculate Precision, Recall, and F-Measure for Imbalanced Classification // machinelearningmastery.com : сайт. – URL: https://machinelearningmastery.com/precision-recall-and-f-measure-forimbalanced-classification/ (дата обращения: 08.06.2023).
47. Transfer learning & fine-tuning // keras.io : сайт. – URL: https://keras.io/guides/transfer_learning/ (дата обращения: 08.06.2023).