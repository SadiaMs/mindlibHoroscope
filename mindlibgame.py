import streamlit as st
import time
import random

# 🎭 Motivational Messages
motivational_quotes = [
    "🌟 **Your mind is like a parachute—it works best when open!**",
    "🚀 **Mistakes are proof that you are trying. Keep going!**",
    "🎭 **Laughter is the best therapy, and it's free! (Unless you're paying a therapist for it!)**",
    "💡 **You are braver than you believe, stronger than you seem, and smarter than you think!**",
    "🎉 **Life is 10% what happens to you and 90% how you react to it. So react like a boss!**"
]

# 🤣 Funny Endings
funny_endings = [
    "😂 And that's how **{name}** became the next horoscope guru!",
    "😱 Suddenly, a talking parrot appeared and said, '**Trust the universe!**' 🦜",
    "🤣 Turns out **{name}** was reading last year's horoscope... Oops!",
    "🚀 **{name}** then started a YouTube channel called 'Astro Vibes & Fries'. 🍟",
    "🤔 And that's when **{name}** realized... horoscopes are just really poetic guesses! 😆"
]

# 🔮 Horoscope Predictions
horoscopes = {
    "Aries": "🔥 Your energy is unstoppable today! Take risks but stay patient.",
    "Taurus": "🌿 A peaceful day ahead. Treat yourself with something sweet!",
    "Gemini": "🗣️ Communication is key! Share your ideas and listen carefully.",
    "Cancer": "💖 Emotions are strong today. Call a loved one for support.",
    "Leo": "🌞 You are shining bright! A great day to take bold actions.",
    "Virgo": "📋 Organization is your superpower today! Make a to-do list.",
    "Libra": "⚖️ Balance is important. Avoid drama and focus on harmony.",
    "Scorpio": "🕵️‍♂️ A mystery unfolds! Trust your instincts and go deep.",
    "Sagittarius": "🏹 Adventure calls! Take a break and explore something new.",
    "Capricorn": "🏆 Hard work pays off. Keep pushing forward with confidence.",
    "Aquarius": "🌊 A wave of creativity is coming! Express yourself freely.",
    "Pisces": "🎭 Dream big! Today is a day to visualize your future."
}

# 🌙 Streamlit UI
st.title("🔮 Horoscope Mad Libs Game 🎭")
st.title("Assalam u Alaikum! 🤝")
st.write("🕌 ** Let's see what the stars say about you today.**")
st.divider()

# 📝 User Inputs
name = st.text_input("💬 Enter your name:")
age = st.number_input("📅 Enter your age:", min_value=1, max_value=120, step=1)
dob = st.date_input("🎂 Enter your date of birth:")
zodiac_sign = st.selectbox("♈ Choose your Zodiac sign:", list(horoscopes.keys()))
favorite_color = st.color_picker("🎨 Pick your favorite color:")
emotion = st.text_input("😊 How are you feeling today? (e.g., happy, excited, stressed)")
activity = st.text_input("🎨 What's one thing you love doing? (e.g., dancing, reading)")
object1 = st.text_input("🕰️ Name a random object near you:")
psych_term = st.text_input("🧠 Enter a psychology term (e.g., subconscious, cognitive bias)")

# 🟢 Button to Generate Horoscope
if st.button("🔮 Reveal My Horoscope"):
    with st.spinner("✨ Consulting the stars..."):
        time.sleep(2)  # ⏳ Fake Loading Effect

    # 📜 Horoscope & Motivational Ending
    horoscope_message = horoscopes.get(zodiac_sign, "The stars seem confused! 😆")
    funny_ending = random.choice(funny_endings).format(name=name)
    motivational_message = random.choice(motivational_quotes)

    # 📖 Horoscope Story
    story = f"""
    🎭 **Hello {name}! Your Horoscope for today:**  

    🔮 **{zodiac_sign} - {horoscope_message}**  

    🌟 You woke up feeling **{emotion}**. To relax, you spent time **{activity}**.  
    While doing so, you found an old **{object1}** that reminded you of **{psych_term}**.  
    It made you reflect on life's mysteries.  

    {funny_ending}  

    ✨ **Motivational Thought:** {motivational_message}  
    """

    st.success("🌟 Your Horoscope & Psychology Story:")
    st.write(story)

# 🎓 Footer
st.divider()
st.title("👩‍🎓 Sadia 370350")
st.write("📚 **Student at GIAIC Khi**")
st.write("🎭 **Horoscope Mad Libs Game** 🔮")
