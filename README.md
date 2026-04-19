```bash
 docker run -v $(pwd):/data plantuml/plantuml -tsvg misc/mindmap.puml
```

## Convert Reports to DOCX

Convert all markdown files in the `report/` folder to DOCX format using Pandoc and save them in the `output/` folder:

```bash
mkdir -p output && for file in report/*.md; do pandoc "$file" -o "output/$(basename "$file" .md).docx"; done
```