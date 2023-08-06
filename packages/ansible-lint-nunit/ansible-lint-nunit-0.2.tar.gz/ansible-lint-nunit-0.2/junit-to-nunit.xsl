<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xalan="http://xml.apache.org/xslt">
    <xsl:output method="xml" indent="yes" xalan:indent-amount="4" cdata-section-elements="message stack-trace"/>

    <xsl:template match="/">
        <test-results name="{//testsuite[1]/@name}" total="{count(//testcase)}" failures="{count(//error) + count(//failure)}" not-run="{count(//skipped)}" time="{//testsuite[1]/@time}">
            <xsl:apply-templates select="testcase"/>
            <xsl:apply-templates select="testsuite"/>

            <xsl:for-each select="testsuites">
                <xsl:apply-templates select="testcase"/>
                <xsl:apply-templates select="testsuite"/>
            </xsl:for-each>
        </test-results>
    </xsl:template>

    <xsl:template match="testcase">
        <xsl:variable name="asserts">
            <xsl:choose>
                <xsl:when test="@assertions != ''">
                    <xsl:value-of select="@assertions"></xsl:value-of>
                </xsl:when>
                <xsl:when test="count(skipped) > 0"></xsl:when>
                <xsl:when test="count(*) > 0">0</xsl:when>
                <xsl:otherwise>1</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="time">
            <xsl:choose>
                <xsl:when test="count(skipped) > 0"></xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select="@time"></xsl:value-of>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="success">
            <xsl:choose>
                <xsl:when test="count(skipped) > 0"></xsl:when>
                <xsl:when test="count(*) > 0">False</xsl:when>
                <xsl:otherwise>True</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="executed">
            <xsl:choose>
                <xsl:when test="count(skipped) > 0">False</xsl:when>
                <xsl:otherwise>True</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="result">
            <xsl:choose>
                <xsl:when test="count(skipped) > 0">Skipped</xsl:when>
                <xsl:when test="count(*) > 0">Failure</xsl:when>
                <xsl:otherwise>Success</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <test-case name="{@name}" description="{@classname}" success="{$success}" time="{$time}" executed="{$executed}" asserts="{$asserts}" result="{$result}">
            <xsl:if test="@classname != ''">
                <categories>
                    <category name="{@classname}" />
                </categories>
            </xsl:if>

            <xsl:apply-templates select="error"/>
            <xsl:apply-templates select="failure"/>
            <xsl:apply-templates select="skipped"/>
        </test-case>
    </xsl:template>

    <xsl:template match="testsuite">
        <xsl:variable name="success">
            <xsl:choose>
                <xsl:when test="count(//testcase/*) > 0">False</xsl:when>
                <xsl:otherwise>True</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="asserts">
            <xsl:choose>
                <xsl:when test="@assertions != ''">
                    <xsl:value-of select="@assertions"></xsl:value-of>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select="count(//testcase) - count(//testcase/*)"></xsl:value-of>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <test-suite name="{@name}" description="{@file}" success="{$success}" time="{@time}" asserts="{$asserts}">
            <xsl:if test="@file != ''">
                <categories>
                    <category name="{@file}" />
                </categories>
            </xsl:if>
            <results>
                <xsl:apply-templates select="testcase"/>
                <xsl:apply-templates select="testsuite"/>
            </results>
        </test-suite>
    </xsl:template>

    <xsl:template match="error">
        <xsl:variable name="message">
            <xsl:choose>
                <xsl:when test="@message != ''">
                    <xsl:value-of select="@message"></xsl:value-of>
                </xsl:when>
                <xsl:when test="@type != ''">
                    <xsl:value-of select="@type"></xsl:value-of>
                </xsl:when>
                <xsl:otherwise>No message</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="stacktrace">
            <xsl:choose>
                <xsl:when test="text() != ''">
                    <xsl:value-of select="text()"></xsl:value-of>
                </xsl:when>
                <xsl:when test="@type != ''">
                    <xsl:value-of select="@type"></xsl:value-of>
                </xsl:when>
                <xsl:otherwise>No stack trace</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <failure>
            <message><xsl:value-of select="$message"></xsl:value-of></message>
            <stack-trace><xsl:value-of select="$stacktrace"></xsl:value-of></stack-trace>
        </failure>
    </xsl:template>

    <xsl:template match="failure">
        <xsl:variable name="message">
            <xsl:choose>
                <xsl:when test="@message != ''">
                    <xsl:value-of select="@message"></xsl:value-of>
                </xsl:when>
                <xsl:when test="@type != ''">
                    <xsl:value-of select="@type"></xsl:value-of>
                </xsl:when>
                <xsl:otherwise>No message</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xsl:variable name="stacktrace">
            <xsl:choose>
                <xsl:when test="text() != ''">
                    <xsl:value-of select="text()"></xsl:value-of>
                </xsl:when>
                <xsl:when test="@type != ''">
                    <xsl:value-of select="@type"></xsl:value-of>
                </xsl:when>
                <xsl:otherwise>No stack trace</xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <failure>
            <message><xsl:value-of select="$message"></xsl:value-of></message>
            <stack-trace><xsl:value-of select="$stacktrace"></xsl:value-of></stack-trace>
        </failure>
    </xsl:template>

    <xsl:template match="skipped">
        <reason>
            <message>Skipped</message>
        </reason>
    </xsl:template>
</xsl:stylesheet>