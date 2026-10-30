# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from io import StringIO

from varcode import EffectCollection, iter_candidate_effects
from varcode.cli import make_variants_parser, variant_collection_from_args

from .data import (
    cancer_driver_gene_id_set,
    class1_mhc_gene_id_set,
    interferon_response_gene_id_set,
)

parser = make_variants_parser()

out_group = parser.add_argument_group("output")
out_group.add_argument(
    "--output-text",
    default=None,
    help="Name of text output file")

def main(args_list=None):
    if args_list is None:
        args_list = sys.argv[1:]
    args = parser.parse_args(args_list)

    variants = variant_collection_from_args(args)
    all_effects = variants.effects()

    coding_effects = EffectCollection(effect for effect in all_effects if any(
        candidate is not None and candidate.modifies_protein_sequence is True
        for candidate in iter_candidate_effects(effect)))
    coding_effects_per_variant = coding_effects.top_priority_effect_per_variant()

    with StringIO() as string_io:
        for label, count in (
                ("total variants", len(variants)),
                ("# SNVs", sum(v.is_snv for v in variants)),
                ("# indels", sum(v.is_indel for v in variants)),
                ("coding non-synonymous variants", len(coding_effects_per_variant))):
            string_io.write(f"{label:>30}: {count:5d}\n")

        string_io.write("A variant is counted when any candidate changes the protein.\n"
                        "Candidates are predictions, not observed products or probabilities.\n")
        string_io.write("===\n\n")
        for label, gene_ids in (
                ("known cancer", cancer_driver_gene_id_set),
                ("MHC-I presentation", class1_mhc_gene_id_set),
                ("interferon response", interferon_response_gene_id_set)):
            string_io.write(f"\nCoding variants in {label} genes:\n")
            for v, e in coding_effects_per_variant.items():
                if e.gene_id not in gene_ids:
                    continue
                string_io.write(f"-- {e.gene_name} {e.short_description} ({v.short_description})\n")
                candidates = list(iter_candidate_effects(e))
                if len(candidates) > 1:
                    descriptions = [
                        f"{type(c).__name__}: {c.short_description}"
                        if c is not None else "Unresolved: unavailable candidate"
                        for c in candidates]
                    string_io.write(f"   candidate consequences: {'; '.join(descriptions)}\n")
        text = string_io.getvalue()

    print(text)

    if args.output_text:
        with open(args.output_text, "w") as f:
            f.write(text)

