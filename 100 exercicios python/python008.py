v_metro=int(input('insira o valor em metros: '))
km=v_metro/1000
he=v_metro/100
dm=v_metro/10
dc=v_metro*10
cm=v_metro*100
mm=v_metro*1000

print(f"\nValor inserido: {v_metro} m\n")
print(f"Em quilômetros:      {km:.4f} km")
print(f"Em hectômetros:      {he:.4f} hm")
print(f"Em decâmetros:       {dm:.4f} dam")
print(f"Em decímetros:       {dc:.2f} dm")
print(f"Em centímetros:      {cm:.2f} cm")
print(f"Em milímetros:       {mm:.2f} mm")