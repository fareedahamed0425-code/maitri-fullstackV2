import unittest

from providers.sarvam.sarvam_client import build_fallback_response


class RuntimeFallbackTests(unittest.TestCase):
    def test_build_fallback_response_returns_helpful_text(self):
        result = build_fallback_response(
            "I feel overwhelmed and need help right now.",
            language="en-IN",
        )
        self.assertIn("I’m here with you", result)
        self.assertTrue(len(result) > 20)


if __name__ == "__main__":
    unittest.main()
