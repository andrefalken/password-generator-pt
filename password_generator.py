# Import function to choose the characters
from random import choices, choice, randint
import string


# Import the characters module and word list
from word_list import portuguese_words, get_words_by_length, get_words_up_to_length


def password_generator(quantity: int) -> str:
    """
    This function generates a human-readable but secure password
    Format: Word1Word2Word3_SpecialCharacter1234
    parameter quantity: Approximate quantity of password characters
    return: Return a string with the password
    """

    # Calculate how many words we need (each word contributes about 4-8 characters)
    # We want the total to be approximately equal to the requested quantity
    target_length = quantity - 5  # Subtract 5 for special char and 4 digits

    password_parts = []
    current_length = 0

    # Smart word selection based on remaining space
    while current_length < target_length:
        remaining_space = target_length - current_length

        # Prefer words that fit perfectly in the remaining space
        if remaining_space >= 3:
            # Try to get words that match the remaining space
            available_lengths = [l for l in range(3, min(11, remaining_space + 1)) if get_words_by_length(l)]

            if available_lengths:
                # Prefer longer words first, but mix it up
                if remaining_space > 6 and randint(0, 1) == 0:
                    word_length = max(available_lengths)
                else:
                    word_length = choice(available_lengths)

                word = choice(get_words_by_length(word_length))
            else:
                # Fallback to any word that fits
                available_words = [w for w in portuguese_words if len(w) <= remaining_space]
                if available_words:
                    word = choice(available_words)
                else:
                    break
        else:
            # Not enough space for a reasonable word
            break
        # Capitalize the word (first letter uppercase, rest lowercase)
        capitalized_word = word.capitalize()
        password_parts.append(capitalized_word)
        current_length += len(capitalized_word)

        # Don't add too many words if the quantity is small
        if len(password_parts) >= 4 or current_length >= target_length:
            break

    # Join all words together
    password = ''.join(password_parts)

    # Add a special character
    special_characters = "!@#$%&*_-+=?"
    password += choice(special_characters)

    # Add 4 random digits
    password += ''.join(choices(string.digits, k=4))

    # If password is too short, add more words strategically
    while len(password) < quantity - 2 and len(password_parts) < 6:
        remaining_space = quantity - len(password) - 5  # Account for special char and digits

        if remaining_space >= 3:
            available_words = [w for w in portuguese_words if 3 <= len(w) <= remaining_space]
            if available_words:
                word = choice(available_words)
                password += word.capitalize()
            else:
                break
        else:
            break

    # If the password is too long, truncate it intelligently
    if len(password) > quantity:
        # Try to cut at word boundaries if possible
        words = password_parts
        temp_password = ''.join(words)

        if len(temp_password) + 5 <= quantity:  # Special char + 4 digits
            password = temp_password + password[-5:]  # Keep the special char and digits
        else:
            # Cut excess characters from the end of the last word
            excess = len(password) - quantity
            if excess > 0 and len(words) > 1:
                last_word = words[-1]
                if len(last_word) > excess + 2:  # Keep at least 2 chars of the last word
                    new_last_word = last_word[:-excess]
                    words[-1] = new_last_word
                    password = ''.join(words) + password[-5:]
                else:
                    # Remove the last word entirely
                    words = words[:-1]
                    password = ''.join(words) + password[-5:]
            else:
                password = password[:quantity]

    return password


def generate_efficient_password(quantity: int) -> str:
    """
    More efficient version that uses word length optimization
    """
    # Define target components
    target_words_length = quantity - 5

    # Select words that sum up close to the target length
    words = []
    current_length = 0

    while current_length < target_words_length:
        remaining = target_words_length - current_length

        # Smart word length selection
        if remaining >= 8:
            word_length = choice([6, 7, 8])
        elif remaining >= 6:
            word_length = choice([4, 5, 6])
        elif remaining >= 4:
            word_length = choice([3, 4])
        else:
            break

        available_words = get_words_by_length(word_length)
        if available_words:
            word = choice(available_words)
            words.append(word.capitalize())
            current_length += len(word)
        else:
            break

        # Limit number of words
        if len(words) >= 4:
            break

    # Fallback if no words selected
    if not words:
        words = ["Secure", "Code"]

    password = ''.join(words)

    # Add special character and digits
    special_characters = "!@#$%&*_-+=?"
    password += choice(special_characters)
    password += ''.join(choices(string.digits, k=4))

    # Final length adjustment
    if len(password) > quantity:
        password = password[:quantity]

    return password


# Test function
if __name__ == '__main__':
    print("🔐 Testing Password Generator with Expanded Word List")
    print("=" * 50)

    test_lengths = [12, 16, 20, 24, 30]

    for length in test_lengths:
        password = generate_efficient_password(length)
        strength = "Strong" if len(password) >= 12 and any(c.isupper() for c in password) and any(
            c.isdigit() for c in password) else "Medium"
        print(f"{length:2d} chars: {password} ({strength})")

    print(f"\n📊 Word list contains {len(portuguese_words)} words")

    # Show word length distribution
    from collections import Counter

    length_dist = Counter(len(word) for word in portuguese_words)
    print("📈 Word length distribution:")
    for length, count in sorted(length_dist.items()):
        print(f"  {length} characters: {count} words")