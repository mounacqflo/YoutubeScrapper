from youtube_scrapper import Scrapper
import unittest

class TestScrapingMethods(unittest.TestCase):

    def testTitre_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedTitre = "Ruud vs. Fritz | Nitto ATP Finals Highlights"
        titre = scrapper.getTitre()
        self.assertEqual(titre, expectedTitre)

    def testTitre_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedTitre = "Ruud vs. Fritz | Nitto ATP Finals Highlights - YouTube"
        titre = scrapper.getTitre()
        self.assertEqual(titre, expectedTitre)

    def testVideaste_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedVideaste = "ATP Tour"
        videaste = scrapper.getVideaste()
        self.assertEqual(videaste, expectedVideaste)

    def testVideaste_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedVideaste = "WTA Tour"
        videaste = scrapper.getVideaste()
        self.assertEqual(videaste, expectedVideaste)

    def testPoucesBleu_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedPoucesBleu = "86"
        poucesBleu = scrapper.getPoucesBleu()
        self.assertEqual(poucesBleu, expectedPoucesBleu)

    def testPoucesBleu_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedPoucesBleu = "94"
        poucesBleu = scrapper.getPoucesBleu()
        self.assertEqual(poucesBleu, expectedPoucesBleu)

    def testDescription_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedDescription = "It was a dramatic, late-night ending in Torino as Casper Ruud battled it out against Taylor Fritz.\n\nSUBSCRIBE: http://bit.ly/2dj6EhW\n\nWEBSITE: http://www.atptour.com/\nFACEBOOK: https://www.facebook.com/ATPTour/\nTWITTER: https://twitter.com/ATPTour\nINSTAGRAM: https://www.instagram.com/atptour/\n\nAbout the Official ATP Tour YouTube Channel:\nAs the global governing body of men\u2019s professional tennis, the ATP\u2019s mission is to serve tennis. We entertain a billion global fans, showcase the world\u2019s greatest players at the most prestigious tournaments, and inspire the next generation."
        description = scrapper.getDescription()
        self.assertEqual(description, expectedDescription)

    def testDescription_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedDescription = "empty description"
        description = scrapper.getDescription()
        self.assertEqual(description, expectedDescription)

    def testLiens_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedLiens = [
            "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkh6MkJ6Y3g3eGZCRlhXZWZ6Q2pxTmkxa1plUXxBQ3Jtc0tsQUk4OVEtUmt3VnBkdVpYQWNjN0d5VmtnYzFPQ0QybzZaRV9hYW5oR2UxV09JZjJ6TmJweUFxSUhlX2JUYlNyNDZBemFHMnF4Wm5OVS10R3V0cUpuVjVhaUNFSVN5bUN6QV90Rm8xME5pYi1ZTnBQaw&q=http%3A%2F%2Fbit.ly%2F2dj6EhW&v=9nThTchFfGc",
            "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa01ydnk1RzFoYzdCTHV1WUtTOWVHOU5VYlBLZ3xBQ3Jtc0trb2cxZHBHTG9rT0tEaGNjX3l4Vzg1ck1EODR2Tmp1TUQ1c243V3llekZFRjJkYzltenZ5MWlORmdmSnZkTGJaQWlnVWlTb1I4aE1MbU1ud2hxZ3pIbmZTeHIwdGpkblctd2pUWS1mai1ya2JSLWMxQQ&q=http%3A%2F%2Fwww.atptour.com%2F&v=9nThTchFfGc",
            "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3FvTmhvZ1hfcV9tU3dRakVmWEF0STlSWjNfUXxBQ3Jtc0trSlhBTjc3ektRZGpaWWVNS1gybEZFMDBnbnBzU21HaG53OU8xZ0FNTkdTeG5qZS13aWhWQWNuWVNIdmk4T2toQm9mMWJHWW5FcjJFdHJCYXVoZUFreTdSUTdsMWJSM3U0ZTgtWklIRkJ4emhXU0Zxbw&q=https%3A%2F%2Fwww.facebook.com%2FATPTour%2F&v=9nThTchFfGc",
            "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqay1xejZTVUpKZjFERkdIbF8tVWxOeFl5M3NRd3xBQ3Jtc0tsZXF4a1hZQUVic3p2bmM5M0YxM0M3UnpCWDJ6U3Q4M0JWTnF3TlRVOFdFQWYwOFIwRC0tTTJITm00eG4xSlpqQ3lBYnprVkc3a1JMU0REWjdFWWVQejZQSTBQMkxYT3hfQXM4VGdwOExpWEdja3J6cw&q=https%3A%2F%2Ftwitter.com%2FATPTour&v=9nThTchFfGc",
            "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXVQM1N0S1JfaUxoc0RaRjFkdjFNWW1fQ2V6Z3xBQ3Jtc0ttU3I2QVh2VTlHMlpTSGNYcG5IY3MwUmQ1bnc3MnBVdndsQ3JMSVF6VVp1Wm44MW9HSWdYY3ZObnNZcEhoYUJwdVd6cktXQmRsVWNFNVFsRmFYYzZ5N0hvWXNRUnB5VFVMZGNIQi16TDNpU2w0eHc2MA&q=https%3A%2F%2Fwww.instagram.com%2Fatptour%2F&v=9nThTchFfGc"
        ]
        liens = scrapper.getLiens()
        self.assertEqual(liens, expectedLiens)

    def testLiens_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedLiens = []
        liens = scrapper.getLiens()
        self.assertEqual(liens, expectedLiens)

    def testId_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedId = "9nThTchFfGc"
        id = scrapper.getId()
        self.assertEqual(id, expectedId)

    def testId_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedId = "null"
        id = scrapper.getId()
        self.assertEqual(id, expectedId)

    def testComments_v1(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedComments = [
            "Much better highlight selection here than in tennisTV\u2019s \u2026",
            "ruud is guud",
            "Rudy good.",
            "Ruuudiculous!!!",
            "You can't beat Novak from the baseline."
        ]
        comments = scrapper.getComments(10)
        self.assertEqual(comments, expectedComments)

    def testComments_v2(self):
        scrapper = Scrapper()
        scrapper.getDriverAndSoup("9nThTchFfGc")
        expectedComments = []
        comments = scrapper.getComments(10)
        self.assertEqual(comments, expectedComments) 