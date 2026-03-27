# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

This system can create a filter bubble because songs that are closest in energy keep rising to the top, even when mood does not match. During the experiment, I doubled energy weight and cut genre weight in half, and this made high-energy songs dominate many profiles. That is why tracks like Gym Hero still show up for users who asked for happy pop or even conflicting moods, because its energy is close and it also gets genre points for pop. Another limitation is that the catalog is small and mood labels are narrow, so users with uncommon moods or genres get results based mostly on energy distance instead of true taste fit.

---

## 7. Evaluation  

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Edge Case High Energy + Sad Mood, and Edge Case Unknown Genre/Mood. I looked at the top 5 songs and checked whether the reasons matched what the profile asked for. The results were partly accurate and partly just different after the weight shift: genre mattered less, and energy closeness took over the ranking. The most surprising pattern was that Gym Hero kept appearing for multiple profiles, not because it matched mood well, but because its energy is very close to high-energy targets and it is in the pop genre. In plain language, the model is good at matching "vibe intensity" but weaker at understanding emotional intent.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
