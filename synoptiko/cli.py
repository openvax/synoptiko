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

from six import StringIO
from varcode.cli import variant_collection_from_args, make_variants_parser

from .data import (
    cancer_driver_gene_id_set,
    interferon_response_gene_id_set,
    class1_mhc_gene_id_set
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

    coding_effects = all_effects.drop_silent_and_noncoding()
    coding_effects_per_variant = coding_effects.top_priority_effect_per_variant()

    with StringIO() as string_io:
        string_io.write("%30s: %5d\n" % ("total variants", len(variants)))
        string_io.write("%30s: %5d\n" % (
            "# SNVs",
            sum([v.is_snv for v in variants])
        ))
        string_io.write("%30s: %5d\n" % (
            "# indels",
            sum([v.is_indel for v in variants])
        ))

        string_io.write("%30s: %5d\n" % (
            "coding non-synonymous variants",
            len(coding_effects_per_variant)))

        string_io.write("===\n\n")
        string_io.write("\nCoding variants in known cancer genes:\n")
        for v, e in coding_effects_per_variant.items():
            if e.gene_id in cancer_driver_gene_id_set:
                string_io.write("-- %s %s (%s)\n" % (e.gene_name, e.short_description, v.short_description))

        string_io.write("\nCoding variants in MHC-I presentation genes:\n")
        for v, e in coding_effects_per_variant.items():
            if e.gene_id in class1_mhc_gene_id_set:
                string_io.write("-- %s %s (%s)\n" % (e.gene_name, e.short_description, v.short_description))

        string_io.write("\nCoding variants in interferon response genes:\n")
        for v, e in coding_effects_per_variant.items():
            if e.gene_id in interferon_response_gene_id_set:
                string_io.write("-- %s %s (%s)\n" % (e.gene_name, e.short_description, v.short_description))
        text = string_io.getvalue()

    print(text)

    if args.output_text:
        with open(args.output_text, "w") as f:
            f.write(text)

