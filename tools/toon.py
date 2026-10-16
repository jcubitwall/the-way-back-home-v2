#!/usr/bin/env python3
"""Cartoon (2D comic) version of a picture for the cartoon tract: flat colours + ink outlines.
    python3 tools/toon.py art/toon cover garden-clip ...   (reads art/src/<name>.jpg, writes <dir>/<name>.jpg)"""
import cv2, numpy as np, sys
def toon(src, dst, k=16):
    im = cv2.imread(src)
    im = cv2.resize(im, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    sm = im.copy()
    for _ in range(4): sm = cv2.bilateralFilter(sm, 9, 60, 9)
    # flat colours: k-means in Lab
    lab = cv2.cvtColor(sm, cv2.COLOR_BGR2LAB).reshape(-1,3).astype(np.float32)
    _, lbl, cen = cv2.kmeans(lab, k, None, (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 2, cv2.KMEANS_PP_CENTERS)
    q = cen[lbl.flatten()].reshape(sm.shape).astype(np.uint8)
    q = cv2.cvtColor(q, cv2.COLOR_LAB2BGR)
    q = cv2.medianBlur(q, 5)
    # bold ink outlines
    g = cv2.cvtColor(cv2.medianBlur(sm, 7), cv2.COLOR_BGR2GRAY)
    e = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 7)
    e = cv2.erode(e, np.ones((2,2),np.uint8))
    lines = cv2.morphologyEx(255-e, cv2.MORPH_OPEN, np.ones((2,2),np.uint8))
    n, lab2, stats, _ = cv2.connectedComponentsWithStats(lines)
    keep = np.zeros_like(lines)
    for i in range(1,n):
        if stats[i, cv2.CC_STAT_AREA] > 140: keep[lab2==i] = 255
    out = q.copy(); out[keep>0] = (40,30,35)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 86])
for a in sys.argv[2:]:
    toon(f'art/src/{a}.jpg', f'{sys.argv[1]}/{a}.jpg')
