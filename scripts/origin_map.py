import json, csv, argparse, pathlib

def load_ancestry(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)  # [{"region":"British & Irish","pct":32.4}, ...]

def load_lookup(path):
    out = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["region"]] = row
    return out

def make_geojson(ancestry, lookup):
    features = []
    for item in ancestry:
        r = item["region"]
        pct = float(item["pct"])
        if pct <= 0 or r not in lookup:
            continue
        lat = float(lookup[r]["lat"]); lon = float(lookup[r]["lon"])
        features.append({
            "type":"Feature",
            "properties":{"region":r, "pct":pct, "name":lookup[r]["display_name"],
                          "migration_node": lookup[r].get("migration_node","")},
            "geometry":{"type":"Point","coordinates":[lon,lat]}
        })
    return {"type":"FeatureCollection","features":features}

def main():
    ap = argparse.ArgumentParser(description="Build a simple GeoJSON from ancestry summary")
    ap.add_argument("--ancestry", required=True, help="examples/ancestry_example.json")
    ap.add_argument("--lookup", required=True, help="examples/region_lookup.csv")
    ap.add_argument("--out", default="examples/your_lineage.geojson")
    args = ap.parse_args()

    ancestry = load_ancestry(args.ancestry)
    lookup = load_lookup(args.lookup)
    gj = make_geojson(ancestry, lookup)

    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(gj, f, indent=2)
    print(f"Wrote {args.out} with {len(gj['features'])} features.")

if __name__ == "__main__":
    main()
