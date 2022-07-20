 package com.github.mvinesn

 import org.scalatest.FunSuite
 import org.scalatest.MustMatchers

 class TextStatsSpec extends FunSuite with MustMatchers {

   test("Getting stats from empty text") {
     new TextStatsUDF().getTextStats(text = "") must be (0, 0)
   }

   test("Getting stats from non-empty text") {
     new TextStatsUDF().getTextStats(text = "One two three four") must be (4, 18)
   }

   test("Getting stats from texts with multiple blanks") {
     val stats = new TextStatsUDF()
     stats.getTextStats(text = "   One two three four") must be (4, 21)
     stats.getTextStats(text = "One    two three  four") must be (4, 22)
     stats.getTextStats(text = "One two three four   ") must be (4, 21)
     stats.getTextStats(text = "  One two three four   ") must be (4, 23)
     stats.getTextStats(text = "    ") must be (0, 4)
   }

 }