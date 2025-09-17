--- mcr.py (原始代码)
+++ mcr.py (修改后代码)
@@ -1,22 +1,33 @@
 def is_win(game):
     win = False
     # Check rows
-    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
+    # 简化胜利条件判断，统一检查非空且相同
+    def check_line(a, b, c):
+        return a == b == c and a != ' '
+    # 检查行、列、对角线
+    if check_line(game[0][0], game[0][1], game[0][2]):
         win = True
-    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
+    if check_line(game[1][0], game[1][1], game[1][2]):
         win = True
-    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
+    if check_line(game[2][0], game[2][1], game[2][2]):
         win = True
     # Check columns
-    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
+    if check_line(game[0][0], game[1][0], game[2][0]):
         win = True
-    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
+    if check_line(game[0][1], game[1][1], game[2][1]):
         win = True
-    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
+    if check_line(game[0][2], game[1][2], game[2][2]):
         win = True
     # Check diagonals
-    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
+    if check_line(game[0][0], game[1][1], game[2][2]):
         win = True
-    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
+    if check_line(game[0][2], game[1][1], game[2][0]):
         win = True
     return win
 
 def main():
     game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
     player1 = 'X'
     player2 = 'O'
-    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
+    turn = False  # False: Player 1 (X) turn, True: Player 2 (O) turn (Player 1 first)
     print("X = Player 1")
     print("O = Player 2")
+    print("Note: Enter coordinates as 'i j' (e.g., '1 1' for top-left cell), i/j range 1-3")
     for n in range(9):
         turn = not turn  # Switch turns
         if not turn:
             print("Player 1: ", end="")
         else:
             print("Player 2: ", end="")
-        print("Which cell to mark? i:[1..3], j:[1..3]: ")
+        print("Enter cell to mark (i j): ")
         i, j = map(int, input().split())
         i -= 1
         j -= 1
+        # Check if input coordinates are valid (0-2)
+        if i < 0 or i > 2 or j < 0 or j > 2:
+            print("Error: Coordinates must be 1-3! Retry your turn.")
+            turn = not turn  # Keep current player's turn
+            continue
+        # Check if cell is already occupied
+        if game[i][j] != ' ':
+            print("Error: This cell is already marked! Retry your turn.")
+            turn = not turn  # Keep current player's turn
+            continue
         if not turn:
             game[i][j] = 'X'
         else:
             game[i][j] = 'O'
         if is_win(game):
-            print("Win!")
+            print(f"Player {1 if not turn else 2} wins!")  # Clear winner prompt
             break  # Terminate the game
         if n == 8:  # All cells have been filled
             print("Tie!")
         # Show the game board
+        print("Current game board:")
         for row in game:
-            print(" ".join(row))
+            print("| " + " | ".join(row) + " |")  # Add board borders for clarity
             print('1')
