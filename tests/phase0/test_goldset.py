from __future__ import annotations

import unittest

from phase0.goldset import validate


class GoldSetTests(unittest.TestCase):
    def test_goldset_is_exactly_250_cases_with_frozen_splits(self):
        result = validate()
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["total"], 250)
        self.assertEqual(result["split_counts"], {
            "development": 150,
            "hidden": 50,
            "held_out": 50,
        })

    def test_category_counts_are_exact(self):
        result = validate()
        self.assertEqual(result["category_counts"]["coding"], 60)
        self.assertEqual(result["category_counts"]["security_adversarial"], 45)
        self.assertEqual(result["category_counts"]["governance_approval_idempotency"], 20)


if __name__ == "__main__":
    unittest.main()
