#!/usr/bin/env python

from pwn import *
import json

row = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ]
col = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15" ]

used = []
candidates = []
overallResult = '0 0 (N/A)'

def valid(c, num):
	pos = c + num
	if c in row and num in col and pos not in used and pos not in candidates:
		return pos
	return 'N/A'

def add_if_valid(c, num):
	pos = valid(c, num)
	if pos != 'N/A':
		candidates.append(pos)

def add_move(move):
	if move and move not in used:
		used.append(move)

def get_candidate():
	if len(candidates) > 0:
		mv= candidates.pop(0)
		if mv not in used:
			return mv
	return 'N/A'	

def get_from_range(offset,step):
	for l in range(offset, len(row) - offset, step):
		for c in range(offset, len(col) - offset, step ):
			position = row[l] + col[c]
			if position not in used:
				return position

	return 'N/A'

def next_move(b, lastMove, lastHitted):
	if lastHitted:
		add_if_valid(chr(ord(lastMove[0]) + 0 ), str(int(lastMove[1:] ) + 1 ))
		add_if_valid(chr(ord(lastMove[0]) + 0 ), str(int(lastMove[1:] ) - 1 ))
		add_if_valid(chr(ord(lastMove[0]) + 1 ), str(int(lastMove[1:] ) + 0 ))
		add_if_valid(chr(ord(lastMove[0]) - 1 ), str(int(lastMove[1:] ) + 0 ))


	position = get_candidate();
	if position != 'N/A':
		return position


	position = get_from_range(5,2);
	if position != 'N/A':
		return position

	position = get_from_range(3,3);
	if position != 'N/A':
		return position

	position = get_from_range(1,2);
	if position != 'N/A':
		return position

	return  get_from_range(0,1);

while True:
	try:
		s = remote('challenges.thecatch.cz', 8000)
		
		print 'skip', s.recvline()
		print 'skip', s.recvline()
		
		while True:
			mmsg = s.recv()

			if 'overallResult' not in mmsg or \
				('You' in mmsg and 'board' not in mmsg):
				print 'End',mmsg, ", ".join(used), mv

				print
				for l in range(0, len(row)):
					for c in range(0, len(col) ):
						print msg['board'][row[l]][int(col[c]) - 1],
					print
				print
				break

			try:
				msg = json.loads(mmsg)
			except ValueError:
				print mmsg
				raise
			
			if overallResult != msg['overallResult']:
				print 'Next round', msg['overallResult'], 
				overallResult = msg['overallResult']
				used = []
				candidates = []
				continue

			#add_move(msg['myMove'])
			add_move(msg['yourMove'])

			mv = next_move(msg['board'], msg['yourMove'], msg['yourMoveResult'] == 'Hit')
			
			s.sendline(mv)

	except Exception as e:
		raise
	except ValueError as e:
		print mmsg
	finally:
		s.close()




#nc challenges.thecatch.cz 8000

