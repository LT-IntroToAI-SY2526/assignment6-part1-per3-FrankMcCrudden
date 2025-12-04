# Assignment 6 Part 1 - Writeup

**Name:** Frank McCrudden  
**Date:** 11/21/2025

---

## Part 1: Understanding Your Model

### Question 1: R² Score Interpretation
What does the R² score tell you about your model? What does it mean if R² is close to 1? What if it's close to 0?

**YOUR ANSWER:**
 R2 means how great of a corelation the two variables have, if it were to equal 1, that means there is a perfect positive correlation between the two variables. If it's close to 0, that means there is no corelation between the two variables.



---

### Question 2: Mean Squared Error (MSE)
What does the MSE (Mean Squared Error) mean in plain English? Why do you think we square the errors instead of just taking the average of the errors?

**YOUR ANSWER:**
The MSE means how close the predictions were to the actual numbers. We square the errors because that way if there is a positive and negative number, they don't cancel eachother out.



---

### Question 3: Model Reliability
Would you trust this model to predict a score for a student who studied 10 hours? Why or why not? Consider:
- What's the maximum hours in your dataset?
- What happens when you make predictions outside the range of your training data?

**YOUR ANSWER:**
Yes, I would trust this model to predict a score for a student who studied for ten hours because with the maximum of my dataset, someone who studied for 9.6 hours got a 93, and when someone studied for 1.5 hours, they got a 17. I believe that it would be able to accurately predict someone who would've studied for 10 hours.




---

## Part 2: Data Analysis

### Question 4: Relationship Description
Looking at your scatter plot, describe the relationship between hours studied and test scores. Is it:
- Strong or weak?
- Linear or non-linear?
- Positive or negative?

**YOUR ANSWER:**
My scatter plot has a strong, linear, positive corelation. It has a strong correlation because it's R2 value is almost 1 at 0.97. Because that value is nearing a whole number, that means it has a strong correlation, additionally, because it's positive 0.97 means it has a positive correlation, and when observing the scatter plot, it shows a line that is straight, and aligns with where a majority of data is. That is why I know that there is a strong, linear, positive corelation between hours studied and tests scores.



---

### Question 5: Real-World Limitations
What are some real-world factors that could affect test scores that this model doesn't account for? List at least 3 factors.

**YOUR ANSWER:**
1. What the student did or didn't study.
2. If the student got enough sleep.
3. If the student arrived to class on time.


---

## Part 3: Code Reflection

### Question 6: Train/Test Split
Why do we split our data into training and testing sets? What would happen if we trained and tested on the same data?

**YOUR ANSWER:**
As the model would go, the model would also learn how to analise the data, instead of being able to understand how to read the data, and then knowing what to do with all the data from the start.



---

### Question 7: Most Challenging Part
What was the most challenging part of this assignment for you? How did you overcome it (or what help do you still need)?

**YOUR ANSWER:**
The hardest part for me was making sure I used the x value and y value when I needed to, and not accidently use the wrong one. I just took looking through my program three ties to make sure I didn't mess up.



---

## Part 4: Extending Your Learning

### Question 8: Future Applications
Describe one real-world problem you could solve with linear regression. What would be your:
- **Feature (X):** 
- **Target (Y):** 
- **Why this relationship might be linear:**

**YOUR ANSWER:**
Does sleep (x) would improve learning (y).



---

## Grading Checklist (for your reference)

Before submitting, make sure you have:
- [ ] Completed all functions in `a6_part1.py`
- [ ] Generated and saved `scatter_plot.png`
- [ ] Generated and saved `predictions_plot.png`
- [ ] Answered all questions in this writeup with thoughtful responses
- [ ] Pushed all files to GitHub (code, plots, and this writeup)

---

## Optional: Extra Credit (+2 points)

If you want to challenge yourself, modify your code to:
1. Try different train/test split ratios (60/40, 70/30, 90/10)
2. Record the R² score for each split
3. Explain below which split ratio worked best and why you think that is

**YOUR ANSWER:**
