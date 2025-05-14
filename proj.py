import time
import random

sentences = [
    "Artificial intelligence is the future of technology.",
    "Python is a great programming language for beginners.",
    "Data science involves statistics, coding, and domain knowledge.",
    "Typing fast and accurately is an important skill.",
    "Practice makes a man perfect in every field."
]

def get_random_sentence():
    return random.choice(sentences)

def calculate_wpm(start_time, end_time, typed_text):
    elapsed_time = end_time - start_time
    words = typed_text.strip().split()
    word_count = len(words)
    wpm = (word_count / elapsed_time) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    original_words = original.strip().split()
    typed_words = typed.strip().split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def give_feedback(wpm, accuracy):
    if wpm > 50 and accuracy > 90:
        return "🔥 Excellent typing! Keep it up."
    elif wpm > 40 and accuracy > 80:
        return "✅ Good speed and accuracy. Try to improve a bit more."
    elif accuracy < 70:
        return "⚠ Your speed is okay but accuracy needs work."
    else:
        return "📘 Keep practicing to improve speed and accuracy."

def run_typing_test():
    sentence = get_random_sentence()
    print("\nType the following sentence:\n")
    print(f"📝 {sentence}\n")

    input("Press Enter when you're ready to begin...")
    start_time = time.time()
    typed = input("\nYour input:\n> ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed)
    accuracy = calculate_accuracy(sentence, typed)
    feedback = give_feedback(wpm, accuracy)

    print("\n--- Results ---")
    print(f"Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")
    print(f"Feedback: {feedback}")

def main():
    print("🧠 AI Typing Speed & Accuracy Trainer")

    while True:
        input("\nPress Enter to start...")
        run_typing_test()

        again = input("\nDo you want to practice more? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for practicing! Goodbye.")
            break
# 
if __name__ == "__main__":
    main()