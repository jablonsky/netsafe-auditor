from pathlib import Path
import sys

def resource_path(*parts):

	''' 
	Build an absolute path to a project resource file.
	Works with development and later with PyInstaller.
	'''

	if getattr(sys, 'frozen', False):
		base_path = Path(sys.MEIPASS)
	else:
		base_path = Path(__file__).resolve().parents[1]
	return base_path.joinpath(*parts)

	
