import win32gui as _w32g
import cv2 as _cv2
import numpy as _np
import pyautogui as _pag
import pytesseract as _pyt

_c = "bin/title.config"
_i = "bin/image.png"

def _f(t):
    h = _w32g.FindWindow(None, t)
    if h:
        print(f"Found window: {t} with handle: {h}")
        return h
    else:
        print(f"No window found with title: {t}")
        return None

def _r(f):
    try:
        with open(f, 'r') as _f:
            t = _f.readline().strip()
        return t
    except FileNotFoundError:
        print(f"File not found: {f}")
        return None

def _f_img(p):
    s = _np.array(_pag.screenshot())
    s = _cv2.cvtColor(s, _cv2.COLOR_RGB2BGR)
    t = _cv2.imread(p, _cv2.IMREAD_UNCHANGED)
    r = _cv2.matchTemplate(s, t, _cv2.TM_CCOEFF_NORMED)
    _, mv, _, ml = _cv2.minMaxLoc(r)
    th = 0.8
    if mv >= th:
        print(f"Found image at location: {ml}")
        return ml
    else:
        print("Image not found on screen")
        return None

def _e(p, l="eng+tha"):
    i = _cv2.imread(p)
    g = _cv2.cvtColor(i, _cv2.COLOR_BGR2GRAY)
    t = _pyt.image_to_string(g, lang=l)
    return t

_wt = _r(_c)

if _wt:
    _h = _f(_wt)
    if _h:
        _il = _f_img(_i)
        if _il:
            _et = _e(_i)
            print(f"Extracted Text:\n{_et}")