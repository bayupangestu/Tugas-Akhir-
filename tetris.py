from random import randrange as rand
import pygame as pg
import sys

cell_size =	23
column =	15
row =		27

tetris_shapes = [
	[[1, 1, 1],
	 [0, 1, 0]],
	
	[[0, 2, 2],
	 [2, 2, 0]],
	
	[[3, 3, 0],
	 [0, 3, 3]],
	
	[[4, 0, 0],
	 [4, 4, 4]],
	
	[[0, 0, 5],
	 [5, 5, 5]],
	
	[[6, 6, 6, 6]],
	
	[[7, 7],
	 [7, 7]]
]

def remove_row(board, row):
	del board[row]
	return [[0 for i in xrange(column)]] + board

def new_board():
	board = [ [ 0 for x in xrange(column) ]
			for y in xrange(row) ]
	board += [[ 1 for x in xrange(column)]]
	return board

class TetrisApp(object):
	def __init__(self):
		pg.init()
		pg.key.set_repeat(250,25)
		self.width = cell_size*(column+6)
		self.height = cell_size*row
		self.rlim = cell_size*column
		self.bground_grid = [[ 8 if x%2==y%2 else 0 for x in xrange(column)] for y in xrange(row)]

		self.default_font =  pg.font.Font(
			pg.font.get_default_font(), 12)
		
		self.screen = pg.display.set_mode((self.width, self.height))
		self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
		self.init_game()

	def start (self):
		if self.gameover:
			self.init_game()
			self.gameover = False
	
	def init_game(self):
		self.board = new_board()
		self.new_stone()
		self.level = 1
		self.score = 0
		self.lines = 0
		pg.time.set_timer(pg.USEREVENT+1, 1000)
		
	def new_stone(self):
		self.stone = self.next_stone[:]
		self.next_stone = tetris_shapes[rand(len(tetris_shapes))]
		self.stone_x = int(column / 2 - len(self.stone[0])/2)
		self.stone_y = 0
	
	def run(self):
		key_actions = {

		}
		
		self.gameover = False
		self.paused = False

		
		
		

if __name__ == '__main__':
	App = TetrisApp()
	App.run()