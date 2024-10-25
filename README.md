# 📚 DiverEdu: Personalized Content Generation for Neurodivergent Students

**DiverEdu** is a project aimed at creating personalized educational content using generative AI to support neurodivergent students, particularly those with **dyslexia**, **dyscalculia**, and **ADHD**. The project focuses on improving accessibility and fostering empathy in the classroom.

## 🌟 Key Features

### 1. 🧩 Content Generation for Neurodivergent Students

#### 📝 Dyslexia Support
For students with dyslexia, DiverEdu adds **emojis** next to difficult words, providing a visual cue to assist in word comprehension. This makes the reading process easier and more engaging.

#### 🎯 ADHD Support
For students with ADHD, DiverEdu integrates the **Bionic Reading** method, which highlights parts of words to improve focus and comprehension, making it easier to maintain attention on the text.

### 2. 🫂 Empathy Exercises for Classroom Inclusion
DiverEdu includes empathy-building exercises to help neurotypical students understand the challenges their neurodivergent classmates face. Some of these activities include:

- **🔢 Unsolvable math problems**: To simulate the frustrations caused by dyscalculia.
- **🔡 Disordered or misspelled text**: To mimic reading difficulties faced by students with dyslexia.

These exercises aim to foster a supportive and inclusive classroom environment by encouraging understanding and collaboration among students.

---

## 🛠️ Project Structure

### 📱 `front`
This is the **front-end module** that provides the app's user interface, built using **Vue.js**. It uses **Pinia** for state management and data persistence, allowing users to interact with the platform seamlessly.

### 🔗 `generation-api`
This is the **API module**, built with **Flask**. It provides endpoints for generating personalized content, including adaptive text for dyslexia and ADHD, as well as empathy exercises for neurotypical students.

### 🐳 Docker Compose
DiverEdu is deployed using **Docker Compose**, with each module (front and generation-api) having its own Dockerfile for simplified deployment.

---

## 🧠 Scientific Foundations

The development of DiverEdu is firmly rooted in scientifically validated research and established pedagogical practices that are especially effective for neurodivergent learners. The following approaches are supported by peer-reviewed studies, offering a robust foundation for DiverEdu’s methodologies:

#### 1. Bionic Reading
This method enhances reading for dyslexic individuals by emphasizing certain parts of words, improving both speed and comprehension. Research in cognitive science supports the effectiveness of this approach for neurodivergent learners.
- **Relevant Study**: ["The Effect of Contrast on Reading Speed in Dyslexia"](https://www.sciencedirect.com/science/article/pii/S0042698900000419). This study explores how visual cues like contrast impact the reading performance of dyslexic individuals, offering significant insights into the benefits of altered text presentation.

#### 2. Image-Based Learning for ADHD
Visual aids are particularly beneficial for learners with ADHD, improving focus, comprehension, and retention. This method has been shown to effectively replace certain words with images, helping younger children maintain attention during learning tasks.
- **Relevant Study**: ["The Comparison of Visual Perception Skills in ADHD Children"](https://services.brieflands.com/cdn/serve/4f/c5/4fc5071e79ad1bb09c18ac4e72484a0d0b04e372/jbm-In_Press-In_Press-7995.pdf), which demonstrates how children with ADHD benefit from visual learning strategies, making them ideal for classroom and educational settings.

#### 3. Neurodivergent Game Design
Game-based learning fosters the development of social skills and empathy, creating inclusive classroom environments. Research has demonstrated that tailored games can significantly promote social inclusion and emotional growth among neurodivergent learners.
- **Relevant Study**: ["Deal Me In: An Inclusive Lens on Digital Storytelling and Game-Based Learning"](https://repositorio-aberto.up.pt/bitstream/10216/134448/2/479282.pdf). This research outlines how game-based learning promotes empathy, inclusivity, and social engagement in both children and adults.

By integrating these methodologies, DiverEdu provides a scientifically-backed, inclusive learning experience for neurodivergent students.

---

## 🚀 Future Plans

### 🤖 Local AI Model Integration
We plan to integrate a local AI model using **Hugging Face** and **Transformers**. This will reduce operational costs by avoiding reliance on external APIs for content generation.

### 🎯 Fine-Tuning for Improved Accuracy
We also aim to perform **fine-tuning** on the AI model to enhance the accuracy of the generated content, providing more personalized learning materials.

---

## 👥 Developers

- **Daniel Mulas Fajardo** - (https://github.com/danimulas)
- **Mario Prieta Sánchez** - (https://github.com/mariops03)
- **Tomás Pérez Vellarino** - (https://github.com/Tomypv)
- **David Sánchez Sánchez** - (https://github.com/DavidSanSan110)