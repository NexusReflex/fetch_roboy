import board
import adafruit_dotstar as dotstar
dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.2)

dots[0] = (255, 0, 0)
