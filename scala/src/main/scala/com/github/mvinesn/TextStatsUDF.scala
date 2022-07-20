package com.github.mvinesn

import org.apache.spark.sql.api.java.UDF1

case class TextStats(wordCount: Int, charCount: Int)

class TextStatsUDF extends UDF1[String, TextStats] {

  def getTextStats(text: String): TextStats = {
    val charCount = text.length
    val strippedText = text.replaceAll(" +", " ").trim()
    val wordCount = if (strippedText.isEmpty) 0 else strippedText.split(" ").length
    TextStats(wordCount, charCount)
  }

  def call(text: String): TextStats = getTextStats(text)

}