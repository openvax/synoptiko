import pytest

from synoptiko import cli


def test_empty_vcf_produces_zero_counts(tmp_path, capsys):
    vcf = tmp_path / "empty.vcf"
    vcf.write_text("##fileformat=VCFv4.2\n"
                   "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
    output = tmp_path / "summary.txt"
    cli.main(["--vcf", str(vcf), "--genome", "GRCh37", "--output-text", str(output)])
    assert "total variants:     0" in output.read_text()
    assert "coding non-synonymous variants:     0" in output.read_text()
    assert capsys.readouterr().out.strip() == output.read_text().strip()


@pytest.mark.ensembl
def test_intronic_primary_with_coding_alternative_is_reported(monkeypatch, capsys):
    from pyensembl import EnsemblRelease
    from varcode import Variant, VariantCollection
    genome = EnsemblRelease(75)
    variant = Variant("7", 117171171, "A", "C", genome)
    primary = variant.effects().top_priority_effect()
    assert type(primary).__name__ == "Intronic"
    monkeypatch.setattr(cli, "variant_collection_from_args", lambda args: VariantCollection([variant]))
    monkeypatch.setattr(cli, "cancer_driver_gene_id_set", {primary.gene_id})
    # Panel substitution tests the report, not a claim that CFTR is a driver.
    cli.main([])
    text = capsys.readouterr().out
    assert "coding non-synonymous variants:     1" in text
    assert "-- CFTR intronic" in text
    assert "Intronic: intronic" in text
    assert "Deletion:" in text
    assert "Unresolved:" in text
