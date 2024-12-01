---
title: "Imitation Learning 🧏🏻‍"
date: 2024-11-30
draft: false
description: "a description"
tags: ["Wafer Fab", "Imitation Learning"]
---
## Imitation-Learning  {{< badge >}}
Wafer Fab
{{< /badge >}}


In this Notebook is a demo for the imitation learning that learns the pattern to mark some cells 'x' for a semiconductor Wafer dataset , and then mimic the the pattern of the agent to an unseen dataset

The `ImitationLearningCSV` class is a versatile tool for human-in-the-loop machine learning. It enables users to interact with a CSV file, marking and unmarking specific cells. These human-provided annotations serve as valuable training data for a machine learning model. By learning from these expert-provided labels, the model can acquire the ability to predict future markings on similar data.

The class streamlines this process by:

1. **Loading Data:** The `load_existing_data` method seamlessly reads the CSV file into a structured format, making it accessible for further analysis.
2. **Marking and Unmarking:** The `mark_cell` and `unmark_cell` methods allow users to easily designate cells as important or unimportant, providing explicit guidance to the model.
3. **Feature Extraction:** The `extract_features` method extracts relevant features from the marked cells, transforming them into a numerical representation that the machine learning model can understand.
4. **Data Preparation:** The class prepares the extracted features and corresponding labels into a suitable format for training a machine learning model.

By automating these steps, the `ImitationLearningCSV` class significantly simplifies the process of building imitation learning models, making it more accessible to a wider range of users.

The data is related to MFCs  from the Semiconductor Manufacturing tools , and the Lalels for the Aliases are to be Marked by the Agent, 

{{< lead >}}
Check out the sample code on git. 👇🏻
{{< /lead >}}




{{< github repo="akhil4674/Imitation-Learning">}}