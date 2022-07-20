name := """spark-udf"""
version := "0.1.0"

scalaVersion := "2.12.15"
scalacOptions ++= Seq("-unchecked", "-feature", "-deprecation")

val root = project.in(file("."))
  .settings(Seq(
    libraryDependencies ++= Seq(
      "org.scalatest" %% "scalatest" % "3.0.3",
      "org.apache.spark" %% "spark-sql" % "3.3.0"
    ))
  )

assembly / assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}
