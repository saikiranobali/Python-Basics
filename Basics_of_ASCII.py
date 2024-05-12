#ASCII Basics in Python
#chr() method is used to print ASCII character value related to numericals.
#ord() method is used to print ASCII numerical related to given ASCII character.
print("\nUppercase Characters")
for i in range(65,91):
    print(chr(i),end=" ")
print("\nLowercase Characters")
for i in range(97,123):
    print(chr(i),end=" ")
print("\n")
ch1='K'
ch2='i'
print(ord(ch1))
print(ord(ch2))
print("\nCommon symbols:")
for i in range(32, 48):
    print(f"ASCII Value: {i}, Character: {chr(i)}")
for i in range(58, 65):
    print(f"ASCII Value: {i}, Character: {chr(i)}")
for i in range(91, 97):
    print(f"ASCII Value: {i}, Character: {chr(i)}")
for i in range(123, 127):
    print(f"ASCII Value: {i}, Character: {chr(i)}")

#A-Z=65 to 90
#a-z=97 to 122
#Output
# Uppercase Characters
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Lowercase Characters
# a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# 75
# 105
#
# Common symbols:
# ASCII Value: 32, Character:
# ASCII Value: 33, Character: !
# ASCII Value: 34, Character: "
# ASCII Value: 35, Character: #
# ASCII Value: 36, Character: $
# ASCII Value: 37, Character: %
# ASCII Value: 38, Character: &
# ASCII Value: 39, Character: '
# ASCII Value: 40, Character: (
# ASCII Value: 41, Character: )
# ASCII Value: 42, Character: *
# ASCII Value: 43, Character: +
# ASCII Value: 44, Character: ,
# ASCII Value: 45, Character: -
# ASCII Value: 46, Character: .
# ASCII Value: 47, Character: /
# ASCII Value: 58, Character: :
# ASCII Value: 59, Character: ;
# ASCII Value: 60, Character: <
# ASCII Value: 61, Character: =
# ASCII Value: 62, Character: >
# ASCII Value: 63, Character: ?
# ASCII Value: 64, Character: @
# ASCII Value: 91, Character: [
# ASCII Value: 92, Character: \
# ASCII Value: 93, Character: ]
# ASCII Value: 94, Character: ^
# ASCII Value: 95, Character: _
# ASCII Value: 96, Character: `
# ASCII Value: 123, Character: {
# ASCII Value: 124, Character: |
# ASCII Value: 125, Character: }
# ASCII Value: 126, Character: ~