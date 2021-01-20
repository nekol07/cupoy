#!/usr/bin/env python3

import numpy as np

def get_decibel(v1):
	v0 = 20
	return 20 * np.log10(v1/v0)

def get_upa(db):
	v0 = 20
	return 20 * np.power(10, db/v0)

if __name__ == "__main__":
	# 20000 微巴斯卡等於幾分貝
	GdB = get_decibel(20000)
	print(f"GdB = {GdB}")

	# 30 分貝的聲壓會是 50 分貝的幾倍
	uPa_30 = get_upa(30)
	uPa_50 = get_upa(50)
	print(f"30 分貝聲壓：{uPa_30}")
	print(f"50 分貝聲壓：{uPa_50}")
	print(f"相差倍數 : {uPa_30/uPa_50}")
