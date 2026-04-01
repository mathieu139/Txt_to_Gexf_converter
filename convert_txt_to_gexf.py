from pathlib import Path


def txt_to_gexf(txt_file: Path, gexf_file: Path) -> tuple[int, int]:
	nodes = set()
	edges = []

	with txt_file.open("r", encoding="utf-8", errors="ignore") as fin:
		for line in fin:
			line = line.strip()
			if not line or line.startswith("#"):
				continue

			parts = line.split()
			if len(parts) < 2:
				continue

			src = parts[0]
			nodes.add(src)
			for tgt in parts[1:]:
				nodes.add(tgt)
				edges.append((src, tgt))

	with gexf_file.open("w", encoding="utf-8") as fout:
		fout.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		fout.write("<gexf xmlns=\"http://www.gexf.net/1.2draft\" version=\"1.2\">\n")
		fout.write("  <graph mode=\"static\" defaultedgetype=\"undirected\">\n")
		fout.write("    <nodes>\n")

		def sort_key(value: str):
			try:
				return (0, int(value))
			except ValueError:
				return (1, value)

		for node in sorted(nodes, key=sort_key):
			fout.write(f"      <node id=\"{node}\" label=\"{node}\"/>\n")

		fout.write("    </nodes>\n")
		fout.write("    <edges>\n")
		for i, (src, tgt) in enumerate(edges):
			fout.write(f"      <edge id=\"{i}\" source=\"{src}\" target=\"{tgt}\"/>\n")
		fout.write("    </edges>\n")
		fout.write("  </graph>\n")
		fout.write("</gexf>\n")

	return len(nodes), len(edges)


def ask_txt_path() -> Path:
	raw_path = input("Chemin du fichier txt: ").strip().strip('"')
	if not raw_path:
		raise ValueError("Aucun chemin saisi.")

	txt_path = Path(raw_path).expanduser()
	if not txt_path.is_absolute():
		txt_path = (Path.cwd() / txt_path).resolve()

	if not txt_path.exists():
		raise FileNotFoundError(f"Fichier introuvable: {txt_path}")
	if not txt_path.is_file():
		raise FileNotFoundError(f"Le chemin n'est pas un fichier: {txt_path}")
	if txt_path.suffix.lower() != ".txt":
		raise ValueError("Le fichier doit avoir l'extension .txt")

	return txt_path


def main() -> None:
	try:
		input_txt = ask_txt_path()
		output_gexf = input_txt.with_suffix(".gexf")
		node_count, edge_count = txt_to_gexf(input_txt, output_gexf)
	except Exception as exc:
		print(f"Erreur: {exc}")
		return

	print("Conversion terminee.")
	print(f"Source : {input_txt}")
	print(f"Sortie : {output_gexf}")
	print(f"Noeuds : {node_count}")
	print(f"Aretes : {edge_count}")


if __name__ == "__main__":
	main()
