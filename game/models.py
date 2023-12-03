from django.db import models

class GameRoom(models.Model):
    player_x = models.ForeignKey('users.User', related_name='player_x', on_delete=models.CASCADE)
    player_o = models.ForeignKey('users.User', related_name='player_o', on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default=' ' * 9)
    current_turn = models.ForeignKey('users.User', related_name='current_turn', on_delete=models.CASCADE)

    def __str__(self):
        return f"Game Room #{self.id}"
