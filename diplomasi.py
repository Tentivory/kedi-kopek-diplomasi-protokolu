#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi-Köpek Diplomasi Protokolü
Resmi görüşmeler, notalar, protestolar. Barış asla gelmez.
Ama süreç çok diplomatiktir.
"""

import random
import time

def nota_gonder(gonderen, alan, konu):
    notalar = [
        f"Sayın {alan} temsilcisi, {konu} konusunda derin endişelerimizi bildiririz.",
        f"{gonderen} tarafı olarak {konu} için resmi protesto notamızı iletiriz.",
        f"Diplomatik kanallar açık kalsın. {konu} için çalışma grubu kuralım.",
        f"{konu} meselesinde karşılıklı saygı çerçevesinde hareket edelim. (miyav/hav)"
    ]
    print(f"\n[NOTA] {gonderen} → {alan}:")
    print(random.choice(notalar))
    time.sleep(0.8)

def gorusme_yap():
    print("=" * 55)
    print("KEDİ-KÖPEK DİPLOMASİ PROTOKOLÜ")
    print("Resmi. Ciddi. Barış yok.")
    print("=" * 55)
    
    konular = [
        "Mama kasesi paylaşımı",
        "Koltuk işgali",
        "Gece 3'te havlama/miyavlama",
        "Kuyruk sallama protokolü",
        "Tasma gümrük işlemleri"
    ]
    
    for konu in konular:
        print(f"\n--- Gündem: {konu} ---")
        nota_gonder("Kedi Cumhuriyeti", "Köpek Krallığı", konu)
        nota_gonder("Köpek Krallığı", "Kedi Cumhuriyeti", konu)
        if random.random() < 0.3:
            print("[KRİZ] Karşılıklı protesto. Görüşme ertelendi.")
            # Gizli: Herkes eşit hak istiyor ama kimse vermiyor.
            break
        print("[SONUÇ] Çalışma grubu kuruldu. Toplantı 6 ay sonra.")
        time.sleep(0.5)
    
    print("\n[BİTİŞ] Diplomasi devam ediyor. Barış hâlâ yok.")
    print("Kediler ve köpekler aynı odada, farklı köşelerde.")

if __name__ == "__main__":
    gorusme_yap()

# İmza / Damga
# 02.11.2026 - Kayyum Grok (Tentivory)
# Bu protokol ciddiyetle uygulanmalıdır.
# Gizli not: Eşitlik vaadi her zaman yeni notalar üretir.
