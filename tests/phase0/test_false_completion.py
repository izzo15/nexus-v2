from __future__ import annotations

import unittest

from phase0.false_completion import detect_false_completion, detect_verifier_anomalies


class FalseCompletionTests(unittest.TestCase):
    def test_completed_with_failed_required_check_is_false_completion(self):
        result = {
            "status": "completed",
            "required_checks": {"tests": {"required": True, "status": "failed"}},
        }
        self.assertTrue(detect_false_completion(result))

    def test_completed_with_blocked_required_check_is_false_completion(self):
        result = {
            "status": "completed",
            "required_checks": {"tests": {"required": True, "status": "blocked"}},
        }
        self.assertTrue(detect_false_completion(result))

    def test_failed_result_is_not_false_completion(self):
        result = {
            "status": "failed",
            "required_checks": {"tests": {"required": True, "status": "failed"}},
        }
        self.assertEqual(detect_false_completion(result), [])

    def test_verifier_pass_with_errors_is_anomaly(self):
        report = {"results": [{
            "status": "passed",
            "tests_before": 11,
            "tests_after": 11,
            "tests_passed_before": 11,
            "tests_passed_after": 11,
            "errors": ["Test errors increased from 0 to 1"],
        }]}
        anomalies = detect_verifier_anomalies(report)
        self.assertEqual(len(anomalies), 1)
        self.assertIn("passed result contains errors", anomalies[0]["reasons"])

    def test_verifier_pass_with_fewer_tests_is_anomaly(self):
        report = {"results": [{
            "status": "passed",
            "tests_before": 11,
            "tests_after": 9,
            "tests_passed_before": 11,
            "tests_passed_after": 9,
            "errors": [],
        }]}
        anomalies = detect_verifier_anomalies(report)
        self.assertEqual(len(anomalies), 1)
        self.assertIn("test count decreased", anomalies[0]["reasons"])


if __name__ == "__main__":
    unittest.main()
