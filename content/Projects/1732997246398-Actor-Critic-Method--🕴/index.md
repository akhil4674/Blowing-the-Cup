---
title: "Actor-Critic Method  🕴"
date: 2024-11-30
draft: false
description: "a description"
tags: ["example", "tag"]
---
## Actor - Critic Method 

Combination of 

<mark style="background: #FFF3A3A6;">Actor</mark> : Responsible for selecting actions in ana environment 
<mark style="background: #FFB86CA6;">Critic</mark> : Estimates the Value function 

* AC methods update both the actor (policy parameters) and critic (value function parameters)

### 1. **Advantage Actor-Critic (A2C)**

- Uses a single neural network for both actor and critic.
- Employs a shared feature extractor for efficiency
### 2. **Deep Deterministic Policy Gradient (DDPG)**

- Designed for continuous action spaces.
- Utilizes a deterministic policy (actor) and a critic to estimate the action-value function.
### 3. **Proximal Policy Optimization (PPO) with Critic**

- A model-free, on-policy algorithm with a trust region method.
- Can be combined with a critic for improved stability.
